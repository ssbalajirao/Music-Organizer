from pathlib import Path


# Project Directories


PROJECT_ROOT = Path(__file__).resolve().parent.parent

CONFIG_DIR = PROJECT_ROOT / "config"
LOGS_DIR = PROJECT_ROOT / "logs"

SAMPLE_LIBRARY_DIR = PROJECT_ROOT / "sample_library"
INCOMING_DIR = SAMPLE_LIBRARY_DIR / "Incoming"


# Supported Audio Extensions


SUPPORTED_AUDIO_EXTENSIONS = {
    ".mp3",
    ".flac",
    ".m4a",
    ".aac",
    ".wav",
    ".ogg",
    ".opus",
    ".wma",
    ".alac",
}