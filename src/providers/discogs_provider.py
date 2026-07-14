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
