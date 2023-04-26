import spotipy
from spotipy.oauth2 import SpotifyOAuth
import time


def createplaylist(recommendedSongURI,mood_tag):
    # Set up authentication using SpotifyOAuth
    scope = "playlist-modify-public"  # Modify public playlists
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope, client_id="c5520484087e493a9acc091f8d6eda4a", client_secret="3321de158815455cb70ea63c63e8173f",redirect_uri="http://localhost:3000/callback"))

    # Create a new playlist
    playlist_name = str(mood_tag)+ str(time.time())
    playlist_description = "A new playlist created using Spotipy"
    user_id = sp.me()["id"]  # Get current user's ID
    playlist = sp.user_playlist_create(user=user_id, name=playlist_name, description=playlist_description)

    # Add tracks to the playlist
    head='spotify:track:'
    track_uris = []
    for i in recommendedSongURI:
        track_uris.append(head+i)
    sp.playlist_add_items(playlist_id=playlist["id"], items=track_uris)