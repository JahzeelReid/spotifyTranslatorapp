import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Set up Spotify client credentials
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    
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
