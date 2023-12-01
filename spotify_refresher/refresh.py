from spotipy import Spotify
from spotipy.oauth2 import SpotifyOAuth

from spotify_refresher import pl_creators


def refresh():
    scopes = ["playlist-modify-private", "playlist-read-private", 'user-library-read']

    sp = Spotify(auth_manager=SpotifyOAuth(scope=scopes, redirect_uri='http://localhost:8080/callback'))
    pl_creators.top_music_playlist(sp)
    pl_creators.latest_liked_playlist(sp)
    pl_creators.random_liked_playlist(sp)
    pl_creators.new_albums_playlist(sp)
