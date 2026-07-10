from pathlib import Path

from scanner import libraryScanner


def main():
    Scanner = libraryScanner(Path("sample_library/Incoming"))

    albums = Scanner.scan()

    print(f"Albums Found: {len(albums)}")


if __name__ == "__main__":
    main()