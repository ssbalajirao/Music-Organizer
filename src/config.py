import json
from pathlib import Path


CONFIG_FILE = Path(__file__).resolve().parent.parent / "config"/"config.json"


class Config:
    def __init__(self):
        with open(CONFIG_FILE, "r", encoding="utf-8") as file:
            data = json.load(file)

        self.lastfm_api_key = data.get("lastfm_api_key", "")
        # discog isnt using API keys rn 
        # self.musicbrainz_user_agent = data.get(
        #     "musicbrainz_user_agent",
        #     "MusicOrganizer/1.0"
        # )
        # self.discogs_user_token = data.get(
        #     "discogs_user_token",
        #     ""
        # )


config = Config()