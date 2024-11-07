import os
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyOAuth


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
        print(track['name'])
        print(track['artists'][0]['name'])
        print(track['album']['name'])
        print(track['duration_ms']/1000)
        # print(f"Currently playing: {track['name']} by {', '.join([artist['name'] for artist in track['artists']])}")
        return True
    else:
        print("No track currently playing")
        return False


def start_stop():
    # not working might have to do with choosing a device
    # and changing permissions
    sp.start_playback()


def liked_Songs(val):
    for song in sp.current_user_saved_tracks(limit=val)['items']:
        # returns a list of nsted dictionarys
        print(song['track']['name'])

checkPlaying()
