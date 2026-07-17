# from providers.discogs_provider import DiscogsProvider
# from providers.lastfm_provider import LastFMProvider
# import json

# lookup = DiscogsProvider()
# lastfmlookup = LastFMProvider()

# albums = [

#     ("Zach Bryan", "American Heartbreak"),
# ]

# for artist, album in albums:
#     print("-" * 50)
#     print(f"Artist : {artist}")
#     print(f"Album  : {album}")

#     genre = lastfmlookup.get_genre(
#         artist=artist,
#         album=album
#     )

#     print(json.dumps(genre, indent=4))
# -------------------------------------------------------------------------------------------------------


# from genre import GenreResolver
# from models import Album, Track

# resolver = GenreResolver()

# track = Track(
#     path="",
#     title="",
#     artist="Zach Bryan",
#     album="American Heartbreak",
#     album_artist="Zach Bryan",
#     genre=None,
#     disc_number=None,
#     track_number=None,
#     extension=".mp3",
#     duration=0
# )

# album = Album(
#     source_path="",
#     name="American Heartbreak",
#     album_artist="Zach Bryan",
#     genre=None,
#     tracks=[track]
# )

# genres = resolver._lookup_online(album)

# print(genres)


# ------------------------------------------------------------------------------------------------------------------------------------

# from normalizer import GenreNormalizer

# normalizer = GenreNormalizer()

# normalizer._log_unknown_tag("red dirt")
# normalizer._log_unknown_tag("red dirt")
# normalizer._log_unknown_tag("hip-hop")

# print(normalizer.unknown_tags)

# --------------------------------------------------------------------------------------------------------------------------------------------
from pathlib import Path

from transaction import Transaction

transaction = Transaction()

source = Path("sample_library/Incoming/test.txt")
destination = Path("Music Library/Test/test.txt")

result = transaction.transfer_file(source, destination)

print(result)