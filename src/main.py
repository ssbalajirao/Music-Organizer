from pathlib import Path
from constants import INCOMING_DIR
from scanner import libraryScanner




def main():
    Scanner = libraryScanner(Path(INCOMING_DIR))

    albums = Scanner.scan()

    print(f"\nAlbums Found: {len(albums)}\n")

    for album in albums:
        print(album.source_path.name)


if __name__ == "__main__":
    main()