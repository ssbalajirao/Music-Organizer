from models import Album
import requests
from config import config
from collections import Counter
import re
import json


class DiscogsProvider:
    # searching through Discogs for daata 

    def _cleanAlbumName(self, album:str)->str:
        return re.sub(r"\s*\(.*?\)\s*", "", album).strip()
    
    def search_discogs_album(self, artist: str, album: str):

        url = "https://api.discogs.com/database/search"


        params = {
            "type": "master",
            "artist": artist,
            "release_title": self._cleanAlbumName(album)
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
            print(f"Discogs lookup failed: {e}")
            return None
        
    def get_genre(self,artist:str, album:str ) -> list[str] |None:
        data = self.search_discogs_album(artist, album)

        if data is None:
            return None
        
        results = data.get("results",[])
        # print(json.dumps(album_data, indent=4))
        if not results:
            return None
        album_data = results[0]
        genre_data = album_data.get("genre")
        style_data = album_data.get("style")

        print(json.dumps(genre_data, indent=4))
        print(json.dumps(style_data, indent=4))


        genres = []

        if genre_data:
            genres.extend(genre_data)
        
        if style_data:
            genres.extend(style_data)
        
        
        return genres 


