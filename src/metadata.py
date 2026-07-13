from models import Album
from mutagen import File

class MetadataReader:
    # reading meta data 

    def read_album(self, album:Album)-> None:
        for track in album.tracks:
            self._read_track(track)


    def _read_track(self, track):
        audio = File(track.path)

        if audio is None:
            print(f"Could not read: {track.path.name}")
            return
        
        track.title = self._safe_get(
            audio,
            "title",
            "TIT2",
            "©nam"
        )

        track.album = self._safe_get(
            audio,
            "album",
            "TALB",
            "©alb"
        )

        track.album_artist = self._safe_get(
            audio,
            "albumartist",
            "TPE2",
            "aART"
        )

        track.genre = self._safe_get(
            audio,
            "genre",
            "TCON",
            "©gen"
        )
        print(f"Successfully read: {track.path.name}")
        print(f"Title: {track.title}")
        print(f"Artist: {track.album_artist}")
        print(f"Genre metadatafile: {track.genre}")
        print(f"Album: {track.album}")

        

    
    def _safe_get(self, audio, *tag_names):
        if audio.tags is None:
            return None
        
        for tag in tag_names:
            value = audio.tags.get(tag)
            
            if value:
                if isinstance(value, list):
                    return str(value[0])
                return str(value)
            
        return None