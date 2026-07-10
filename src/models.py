from dataclasses import dataclass, field
from pathlib import Path
from typing import Optional


@dataclass
class Track:
        # audio file and meta data
    
    path: Path

    title: Optional[str] = None
    artist: Optional[str] = None
    album: Optional[str] = None
    album_artist: Optional[str] = None
    genre: Optional[str] = None

    disc_number: Optional[int] = None
    track_number: Optional[int] = None

    extension: Optional[str] = None
    duration: Optional[float] = None


@dataclass
class Album:
        # complete album
    source_path: Path

    name: Optional[str] = None
    album_artist: Optional[str] = None
    genre: Optional[str] = None

    tracks: list[Track] = field(default_factory=list)

    destination_path: Optional[Path] = None

    confidence: float = 0.0