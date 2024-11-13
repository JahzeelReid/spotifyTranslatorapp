from lrclib import LrcLibAPI

# Create an instance of the API
api = LrcLibAPI(user_agent="my-app/0.0.1")

# Get lyrics for a track
def getplainLyric(tname, aname, album, len):
    lyrics = api.get_lyrics(
        track_name=tname,
        artist_name=aname,
        album_name=album,
        duration=len,

        # track_name="Look At Me!",
        # artist_name="XXXTENTACION",
        # album_name="Look At Me!",
        # duration=126,
    )
    found_lyrics = lyrics.plain_lyrics
    print("\n".join(found_lyrics.split("\n")[:10]))
    return found_lyrics.split("\n")

def getsyncLyric():
    lyrics = api.get_lyrics(
        track_name="Look At Me!",
        artist_name="XXXTENTACION",
        album_name="Look At Me!",
        duration=126,
    )
    found_lyrics = lyrics.synced_lyrics
    print("\n".join(found_lyrics.split("\n")[:10]))
    return found_lyrics

# getsyncLyric()