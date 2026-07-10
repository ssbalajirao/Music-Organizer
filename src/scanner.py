from pathlib import Path

from models import Album, Track
from constants import SUPPORTED_AUDIO_EXTENSIONS


class LibraryScanner:
        # scanning incomming albums for songs
    
    def __init__(self, incoming_path: Path):
        self.incoming_path = incoming_path

    def scan(self) -> list[Album]:
        # scans incoming and returns album
        

        if not self.incoming_path.exists():
            print("No Albums Found!")
            return []
        

        
        return self._find_album_folders()
    
    def _find_album_folders(self) -> list[Album]:
        albums = []

        for folder in self.incoming_path.iterdir():
            if folder.is_dir():
                album = self._create_album(folder)
                albums.append(album)
        
        return albums
    
    def _create_album(self, folder:Path) -> Album:
        album = Album(
            source_path=folder,
            name=folder.name
        )

        album.tracks = self._find_tracks(folder)

        return album
    
    # finding tracks
    def _find_tracks(self, folder:Path) -> list[Track]:
        # goes through folder to find supported tracks
        tracks =[]


        for file in folder.rglob("*"):
            if file.is_file() and self._is_audio_file(file):
                track = Track(
                    path = file,
                    extension = file.suffix.lower()
                )
                tracks.append(track)
        return tracks
    

    # audio file check

    def _is_audio_file(self, file:Path) -> bool:
        # returns yes or no if file type is supported or not 

        return file.suffix.lower() in SUPPORTED_AUDIO_EXTENSIONS
