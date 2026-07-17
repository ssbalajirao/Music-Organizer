from models import Album
from collections import Counter

from providers.lastfm_provider import LastFMProvider
from providers.discogs_provider import DiscogsProvider
from normalizer import GenreNormalizer

class GenreResolver:
    # determing the genre of the music

    def __init__(self):
        self.lastfm = LastFMProvider()
        self.discogs = DiscogsProvider()
        self.normalizer = GenreNormalizer()


    def _majority_vote(self, album: Album) -> str:
        genres=[]

        for track in album.tracks:
            # print(f"{track.title} -> {track.genre}") 
            if track.genre:
                genres.append(track.genre)
        # print(genres) 
        if not genres:
            return None
        
        counter = Counter(genres)

        # print(counter)

        return counter.most_common(1)[0][0]
    
    # majority vote after majority is done we resolve 
    
    def resolve(self, album: Album) -> str:
        genre = self._majority_vote(album)
        print(f"Majority Vote: {genre}")

        if genre:
            return genre
        # return self._lookup_online(album)
        online = self._lookup_online(album)
        print(f"Online Genre: {online}")
        return online


    def _needs_online_lookup(self, album: Album) -> bool:
        for track in album.tracks:
            if track.genre:
                return False

        return True

    def _lookup_online(self, album: Album) -> str | None:

        if not album.tracks:
            return None
        
        referenceTrack = album.tracks[0]

        lastfm_genres = self.lastfm.get_genre(artist=referenceTrack.album_artist, album= referenceTrack.album)

        discogs_genres = self.discogs.get_genre(artist=referenceTrack.album_artist, album= referenceTrack.album)
        print("LastFM:", lastfm_genres)
        print("Discogs:", discogs_genres)

        genres = []

        if lastfm_genres:
            genres.extend(lastfm_genres)

        if discogs_genres:
            genres.extend(discogs_genres)

        normalized = []

        for tag in genres:
            genre  = self.normalizer.normalize(tag)

            if genre:
                normalized.append(genre)

        if not normalized:
            return None
        counter  = Counter(normalized)

        return counter.most_common(1)[0][0]
        