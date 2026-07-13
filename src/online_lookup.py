from models import Album
import requests
from config import config
from collections import Counter
import re



class onlineGenreLookup:
    # handling the online search

    BASEURL = "https://musicbrainz.org/ws/2"

    def search_album(self, artist: str, album: str):

        headers = {
            "User-Agent": config.musicbrainz_user_agent
        }

        params = {
            "query": f'artist:"{artist}" AND release:"{album}"',
            "fmt": "json"
        }

        response = requests.get(
            f"{self.BASEURL}/release/",
            headers=headers,
            params=params,
            timeout=10
        )

        print("Status Code:", response.status_code)

        data = response.json()

        print(f"Results Found: {data['count']}")

        return data
    

    def _cleanAlbumName(self, album:str)->str:
        return re.sub(r"\s*\(.*?\)\s*", "", album).strip()

    def search_lastfm_album(self, artist: str, album: str):

        url = "https://ws.audioscrobbler.com/2.0/"

        params = {
            "method": "album.getinfo",
            "artist": artist,
            "album": self._cleanAlbumName(album),
            "api_key": config.lastfm_api_key,
            "format": "json"
        }

        try:
            response = requests.get(
                url,
                params=params,
                timeout=10
            )

            response.raise_for_status()

            return response.json()

        except requests.RequestException as e:
            print(f"Last.fm lookup failed: {e}")
            return None
    
    def get_genre(self, artist:str, album:str) -> str | None:
        data = self.search_lastfm_album(artist, album)

        if data is None:
            return None
        album_data = data.get("album")


        # print(json.dumps(album_data, indent=4))


        if not album_data:
            return None
        
        tags_data = album_data.get("tags")

        if not isinstance(tags_data, dict):
            return None
        
        tags = tags_data.get("tag", [])

        if not tags:
            return None
        
        genres = [tag["name"] for tag in tags]

        for tag in tags:
            genres.append(tag["name"])
            # print("genre", tag["name"])

        counter = Counter(genres)

        return counter.most_common(1)[0][0]
