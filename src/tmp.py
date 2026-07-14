from providers.discogs_provider import DiscogsProvider
import json

lookup = DiscogsProvider()

albums = [

    ("Zach Bryan", "American Heartbreak"),
]

for artist, album in albums:
    print("-" * 50)
    print(f"Artist : {artist}")
    print(f"Album  : {album}")

    genre = lookup.search_discogs_album(
        artist=artist,
        album=album
    )

    print(json.dumps(genre, indent=4))
