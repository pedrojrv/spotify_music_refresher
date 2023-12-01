from spotipy import Spotify

from spotify_refresher.utils.playlist import get_playlist_tracks_uris

TOP_SONGS_GLOBAL_PLAYLIST_ID = '37i9dQZEVXbNG2KDcFcKOF'
TOP_50_GLOBAL_PLAYLIST_ID = '37i9dQZEVXbMDoHDwVN2tF'
# viral_50_global = '7c56df97cfdc4334'
# top_songs_mexico = '161a879015f84b89'
# top_50_mexico = 'd095a68459e14566'
# viral_50_mexico = '8f4f8131cf4140d0'

ALL_TOP_PUBLIC_PLAYLISTS = [TOP_SONGS_GLOBAL_PLAYLIST_ID, TOP_50_GLOBAL_PLAYLIST_ID]


def get_all_top_songs_uris(sp: Spotify) -> list:
    """Get all the tracks (uris) from all the top songs playlists.

    Args:
        sp (Spotify): Spotify object.

    Returns:
        list: List of tracks (uris).
    """
    all_top_songs_uris = []
    for playlist_id in ALL_TOP_PUBLIC_PLAYLISTS:
        all_top_songs_uris += get_playlist_tracks_uris(sp, playlist_id)
    return all_top_songs_uris
