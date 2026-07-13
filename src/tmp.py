from online_lookup import onlineGenreLookup

lookup = onlineGenreLookup()

albums = [
    ("Morgan Wallen", "Dangerous: The Double Album"),
    ("Post Malone", "F-1 Trillion: Long Bed"),
    ("Kanye West", "My Beautiful Dark Twisted Fantasy"),
    ("Linkin Park", "Hybrid Theory"),
]

for artist, album in albums:
    print("-" * 50)
    print(f"Artist : {artist}")
    print(f"Album  : {album}")

    genre = lookup.get_genre(
        artist=artist,
        album=album
    )

    print(f"Genre  : {genre}")