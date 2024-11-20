import os
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import lyrictesting as lyrictesting


# Load environment variables from .env file
load_dotenv()

# Get credentials from environment variables
client_id = os.getenv("SPOTIPY_CLIENT_ID")
client_secret = os.getenv("SPOTIPY_CLIENT_SECRET")
# redirect_uri = os.getenv("SPOTIPY_REDIRECT_URI")
scope = os.getenv("SPOTIPY_SCOPE")

# Set up Spotify client credentials
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=client_id,
    client_secret=client_secret,
    redirect_uri='http://localhost:8888/callback',
    scope=scope
))

# Get the currently playing track
def checkPlaying():
    current_track = sp.current_user_playing_track()
    if current_track is not None:
        track = current_track['item']
        
        progress_seconds = current_track['progress_ms'] // 1000
        minutes, seconds = divmod(progress_seconds, 60)
        # print(track['name'])
        # print(track['artists'][0]['name'])
        # print(track['album']['name'])
        # print(track['album'])
        # print(track['album']['images'][0]['url'])
        # print(track['duration_ms']/1000)
        # print(f"Currently playing: {track['name']} by {', '.join([artist['name'] for artist in track['artists']])}")
        return [track['name'], 
                track['artists'][0]['name'], 
                track['album']['name'], 
                track['duration_ms']/1000, 
                track['album']['images'][0]['url'],
                # [minutes, seconds],
                current_track['progress_ms']
                ]
    else:
        print("No track currently playing")
        return None


def start_stop():
    # not working might have to do with choosing a device
    # and changing permissions
    sp.start_playback()


def liked_Songs(val):
    for song in sp.current_user_saved_tracks(limit=val)['items']:
        # returns a list of nsted dictionarys
        print(song['track']['name'])

def litmustest():
    # this function will test if the spotify and
    # lrc api can meld together
    current_track = checkPlaying()
    if current_track:
        return lyrictesting.getplainLyric(current_track[0], current_track[1], current_track[2], current_track[3])
    else: 
        return None
    
def recentlyric(tname, aname, album, dur, target):
    # current_track = checkPlaying()
    arr = lyrictesting.getsyncLyricNew(tname, aname, album, dur)
    # current_track[0], current_track[1], current_track[2], current_track[3]
    # target = current_track[5]
    closestLowest = 0
    closestindex = 0
    # print(arr)
    # print(target)
    for i in range(len(arr)):
        # iterate over the list 
        # will sort another time
        if arr[i][0] > closestLowest and arr[i][0] < target:
            closestLowest = arr[i][0]
            closestindex = i
    print(arr)
    return [arr[closestindex][1]
            # , arr[closestindex + 1][1], arr[closestindex + 2][1]
            ]
    

    
# print(checkPlaying()[5])
# print(recentlyric())
# litmustest()
