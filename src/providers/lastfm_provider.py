from models import Album
import requests
from config import config
from collections import Counter
import re
import json



class LastFMProvider:
    # handling the online search

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
    
    def get_genre(self, artist:str, album:str) -> list[str] | None:
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


            # print("genre", tag["name"])
        return genres
        # counter = Counter(genres)

        # return counter.most_common(1)[0][0]
