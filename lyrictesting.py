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

def getsyncLyric(tname, aname, album, len):
    lyrics = api.get_lyrics(
        track_name=tname,
        artist_name=aname,
        album_name=album,
        duration=len,
    )
    found_lyrics = lyrics.synced_lyrics
    # print("\n".join(found_lyrics.split("\n")[:10]))
    return found_lyrics.split("\n")

def getsyncLyricNew():
    lyrics = api.get_lyrics(
        track_name="Look At Me!",
        artist_name="XXXTENTACION",
        album_name="Look At Me!",
        duration=126,)
    found_lyrics = lyrics.synced_lyrics.split("\n")
    found_lyrics = [s.replace("[", "") for s in found_lyrics]
    found_lyrics = [s.replace("]", "") for s in found_lyrics]
    found_lyrics = [s.split(" ", 1) for s in found_lyrics]
    for i in range(len(found_lyrics)):
        found_lyrics[i][0] = found_lyrics[i][0].replace(":", ".")
        found_lyrics[i][0] = found_lyrics[i][0].replace("'", "")
        found_lyrics[i][0] = found_lyrics[i][0].split(".")
        found_lyrics[i][0][0] = int(found_lyrics[i][0][0])
        found_lyrics[i][0][1] = int(found_lyrics[i][0][1])
        found_lyrics[i][0][2] = int(found_lyrics[i][0][2])
    print(found_lyrics[:3])
    return found_lyrics




getsyncLyricNew()