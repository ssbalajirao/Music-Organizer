from pathlib import Path


class Verifier:
    
    def verify(self, source:Path, destination:Path)-> bool:
        if not source.exists() or not destination.exists():
            return False

        source_size = source.stat().st_size
        destination_size = destination.stat().st_size
        return source_size == destination_size
