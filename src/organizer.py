from pathlib import Path
from constants import LIBRARY_DIR
from models import Album

class Organizer:

    def destination_path(self, album:Album)->Path:
        # print("O:",album.genre)
        # print("O:",album.tracks[0].album_artist)
        # print("O:",album.name)
        return(
            LIBRARY_DIR / album.genre / album.tracks[0].album_artist / album.name
        )
    
    def create_destination(self, album:Album)->None:
        album.destination_path.mkdir(
            parents=True,
            exist_ok=True
        )

