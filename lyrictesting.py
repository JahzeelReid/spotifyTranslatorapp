from lrclib import LrcLibAPI

# Create an instance of the API
api = LrcLibAPI(user_agent="my-app/0.0.1")

# Get lyrics for a track
lyrics = api.get_lyrics(
    track_name="Look At Me!",
    artist_name="XXXTENTACION",
    album_name="Look At Me!",
    duration=126,
)

found_lyrics = lyrics.synced_lyrics or lyrics.plain_lyrics
print("\n".join(found_lyrics.split("\n")[:]))