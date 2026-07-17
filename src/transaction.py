from pathlib import Path
import shutil
from verifier import Verifier
from constants import LIBRARY_DIR
from models import Album

class Transaction:

    def __init__(self):
        self.verifier  = Verifier()

    def transfer_album(self, album):
        
        for track in album.tracks:
            source = track.path 

            relative_path = track.path.relative_to(album.source_path)

            if album.destination_path is None:
                return False

            destination = album.destination_path /relative_path

            success = self.transfer_file(source, destination)

            if not success:
                return False
        return True


    def transfer_file(self, source: Path, destination: Path) -> bool:
        destination.parent.mkdir(
            parents=True,   
            exist_ok=True
        )

        try:
            # copying the file 
            shutil.copy2(source, destination)

            if self.verifier.verify(source, destination):
                return True
            return False
        
        except Exception as e:
            print(f"failed To transfer {source.name}:{e}")
            return False


    def delete_source(self, album):
        pass