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

# Set up Spotify client credentials
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=client_id,
    client_secret=client_secret,
    redirect_uri='http://localhost:8888/callback',
    scope="user-read-currently-playing"
))

# Get the currently playing track
current_track = sp.current_user_playing_track()
if current_track is not None:
    track = current_track['item']
    print(f"Currently playing: {track['name']} by {', '.join([artist['name'] for artist in track['artists']])}")
else:
    print("No track currently playing")
