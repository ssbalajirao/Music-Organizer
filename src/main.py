from pathlib import Path
from constants import INCOMING_DIR
from scanner import LibraryScanner
from metadata import MetadataReader
from genre import GenreResolver




def main():
    Scanner = LibraryScanner(INCOMING_DIR)
    reader = MetadataReader()
    resolver = GenreResolver()

    albums = Scanner.scan()

    print(f"\nAlbums Found: {len(albums)}\n")

    for album in albums:
        # print(f"\nAlbum: {album.name}")
        print(f"\nReading Album: {album.name}")

        # Read metadata for all tracks in this album
        reader.read_album(album)
        album.genre = resolver.resolve(album)

        print(f"\nAlbum: {album.name}")
        print(f"Tracks Found: {len(album.tracks)}")
        print(f"Resolved Genre: {album.genre}")



if __name__ == "__main__":
    main()