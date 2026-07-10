from pathlib import Path

from models import Album


class libraryScanner:
        # scanning incomming albums for songs
    
    def __init__(self, incoming_path: Path):
        self.incoming_path = incoming_path

    def scan(self) -> list[Album]:
        # scans incoming and returns album
        albums = []

        if not self.incoming_path.exists():
            print("No Albums Found!")
            return albums
        
        for folder in self.incoming_path.iterdir():
            if folder.is_dir():
                album = Album(source_path=folder)
                albums.append(album)
        
        return albums