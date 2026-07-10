from pathlib import Path
from constants import INCOMING_DIR
from scanner import LibraryScanner
from metadata import MetadataReader




def main():
    Scanner = LibraryScanner(INCOMING_DIR)
    reader = MetadataReader()

    albums = Scanner.scan()

    print(f"\nAlbums Found: {len(albums)}\n")

    for album in albums:
        # print(f"\nAlbum: {album.name}")
        print(f"\nReading Album: {album.name}")

        # Read metadata for all tracks in this album
        reader.read_album(album)

        print(f"Tracks Found: {len(album.tracks)}")

        for track in album.tracks:

            print(f"   - {track.path.name}")


if __name__ == "__main__":
    main()