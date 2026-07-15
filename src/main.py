from pathlib import Path
from constants import INCOMING_DIR
from scanner import LibraryScanner
from metadata import MetadataReader
from genre import GenreResolver
from organizer import Organizer




def main():
    Scanner = LibraryScanner(INCOMING_DIR)
    reader = MetadataReader()
    resolver = GenreResolver()

    albums = Scanner.scan()
    organizer  = Organizer()

    # print(f"\nAlbums Found: {len(albums)}\n")

    for album in albums:
        # print(f"\nAlbum: {album.name}")
        # print(f"\nReading Album: {album.name}")

        # Read metadata for all tracks in this album
        reader.read_album(album)
        album.genre = resolver.resolve(album)
        album.destination_path = organizer.destination_path(album)
        organizer.create_destination(album)

        # print(f"\nAlbum: {album.name}")
        # print(f"Tracks Found: {len(album.tracks)}")
        print(f"Resolved Genre: {album.genre}")

        print(f"Destination: {album.destination_path}")


if __name__ == "__main__":
    main()