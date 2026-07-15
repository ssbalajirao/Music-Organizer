import json 
from pathlib import Path


class GenreNormalizer:

    def __init__(self):
        self.mapping_file = Path("config/genre_map.json")
        self.unknown_file = Path("data/unknown.json")

        with open(self.mapping_file, "r", encoding="utf-8") as file:
            self.genre_mapping  = json.load(file)
        
        with open(self.unknown_file, "r", encoding="utf-8") as file:
            self.unknown_tags = json.load(file)
        


    def normalize(self, tag:str) ->str | None:
        
        tag = tag.lower().strip()

        for canonical_genre, aliases in self.genre_mapping.items():
            aliases  = [alias.lower() for alias in aliases]

            if tag in aliases:
                return canonical_genre
        self._log_unknown_tag(tag)    
        return None
    
    def _log_unknown_tag(self, tag:str):

        if tag in self.unknown_tags:
            self.unknown_tags[tag]["count"] += 1

        else:
            self.unknown_tags[tag] = {
                "count": 1
            }

        with open(self.unknown_file, "w", encoding="utf-8") as file:
            json.dump(self.unknown_tags, file, indent=4)




        
