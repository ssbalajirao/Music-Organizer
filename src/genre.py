from models import Album
from collections import Counter
from online_lookup import onlineGenreLookup

class GenreResolver:
    # determing the genre of the music

    def __init__(self):
        self.lookup = onlineGenreLookup()

    def _majority_vote(self, album: Album) -> str:
        genres=[]

        for track in album.tracks:
            print(f"{track.title} -> {track.genre}") 
            if track.genre:
                genres.append(track.genre)
        print(genres) 
        if not genres:
            return None
        
        counter = Counter(genres)

        print(counter)

        return counter.most_common(1)[0][0]
    
    # majority vote after majority is done we resolve 
    
    def resolve(self, album: Album) -> str:
        genre = self._majority_vote(album)

        if genre:
            return genre
        return self._lookup_online(album)


    def _needs_online_lookup(self, album: Album) -> bool:
        for track in album.tracks:
            if track.genre:
                return False

        return True

    def _lookup_online(self, album: Album) -> str:
        if not album.tracks:
            return None
        
        referenceTrack = album.tracks[0]

        return self.lookup.get_genre(
            artist= referenceTrack.album_artist,
            album= referenceTrack.album
        )
        