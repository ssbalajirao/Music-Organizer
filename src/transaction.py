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
            
            for file in album.extra_files:
                source = file

                relative_path = source.relative_to(album.source_path)
                destination = album.destination_path / relative_path
                success = self.transfer_file(source, destination)

                if not success:
                    return False
            # self.delete_source(album)
                
        return True


    def transfer_file(self, source: Path, destination: Path) -> bool:
        destination.parent.mkdir(
            parents=True,   
            exist_ok=True
        )

        try:
            # copying the file 
            shutil.copy2(source, destination)

            return self.verifier.verify(source, destination)
        
        except Exception as e:
            print(f"failed To transfer {source.name}:{e}")
            return False


    def delete_source(self, album: Album):
        try:
            shutil.rmtree(album.source_path)

        except Exception as e:
            print(f"Failed to delete {album.source_path}: {e}")