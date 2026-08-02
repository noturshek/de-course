from dotenv import load_dotenv
import os
from spotipy.oauth2 import SpotifyOAuth

load_dotenv()

sp_oauth = SpotifyOAuth(
    client_id=os.getenv("SPOTIFY_CLIENT_ID"),
    client_secret=os.getenv("SPOTIFY_CLIENT_SECRET"),
    redirect_uri=os.getenv("SPOTIFY_REDIRECT_URI"),
    scope="playlist-read-private playlist-read-collaborative",
    open_browser=True,
    cache_path=".spotifycache"
)

token_info = sp_oauth.get_access_token(as_dict=True)

print("\nAccess Token:")
print(token_info["access_token"])

print("\nRefresh Token:")
print(token_info["refresh_token"])
