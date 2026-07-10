from pathlib import Path

from models import Album


class libraryScanner:
        # scanning incomming albums for songs
    
    def __init__(self, incoming_path: Path):
        self.incoming_path = incoming_path

    def scan(self) -> list[Album]:
        # scans incoming and returns album
        
        
        return[]