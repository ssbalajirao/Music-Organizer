from pathlib import Path
from constants import INCOMING_DIR
from scanner import LibraryScanner
from metadata import MetadataReader
from genre import GenreResolver
from organizer import Organizer
from transaction import Transaction




def main():
    Scanner = LibraryScanner(INCOMING_DIR)
    reader = MetadataReader()
    resolver = GenreResolver()

    albums = Scanner.scan()
    organizer  = Organizer()
    transaction = Transaction()
    # print(f"\nAlbums Found: {len(albums)}\n")

    for album in albums:
        # print(f"\nAlbum: {album.name}")
        # print(f"\nReading Album: {album.name}")

        # Read metadata for all tracks in this album
        reader.read_album(album)
        album.genre = resolver.resolve(album)
        print(f"Final Genre: {album.genre}")

        if album.genre is None:
            print(f"Failed to resolve genre for {album.name}")
            continue

        album.destination_path = organizer.destination_path(album)

        print("=" * 50)
        print(f"Album: {album.name}")
        print(f"Genre: {album.genre}")
        organizer.create_destination(album)
        print(album.name)
        print(len(album.tracks))

        for track in album.tracks:
            print(track.path)

        # print("-" * 50)
        success = transaction.transfer_album(album)

        # print(f"\nAlbum: {album.name}")
        # print(f"Tracks Found: {len(album.tracks)}")
        # print(f"Resolved Genre: {album.genre}")

        # print(f"Destination: {album.destination_path}")


if __name__ == "__main__":
    main()