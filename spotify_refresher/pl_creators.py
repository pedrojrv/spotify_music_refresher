from spotipy import Spotify

from spotify_refresher.utils import playlist
from spotify_refresher.utils import user_tracks
from spotify_refresher.utils.top_tracks import get_all_top_songs_uris
from spotify_refresher.utils.artists import get_latest_artist_album_id
from spotify_refresher.utils.albums import get_tracks_uris_in_album

TOP_MUSIC_PLAYLIST = 'Top Music'
LATEST_LIKED_PLAYLIST = 'Latest Liked'
RANDOM_LIKED_PLAYLIST = 'Random Liked'
RELEASE_RADAR_PLAYLIST = 'Release Radar'
NEW_ALBUMS_PLAYLIST = 'New Albums'


def top_music_playlist(sp: Spotify) -> None:
    """Create a playlist with all the top songs from all the top songs playlists.

    Args:
        sp (Spotify): Spotify object.
    """
    all_top_songs_uris = get_all_top_songs_uris(sp)
    playlist_id = playlist.get_playlist_id(sp, TOP_MUSIC_PLAYLIST, create_if_missing=True)
    sp.playlist_replace_items(playlist_id, all_top_songs_uris)


def latest_liked_playlist(sp: Spotify) -> None:
    """Create a playlist with all the latest liked songs.

    Args:
        sp (Spotify): Spotify object.
    """
    latest_liked_tracks_uris = user_tracks.get_users_latest_liked_tracks_uris(sp)
    playlist_id = playlist.get_playlist_id(sp, LATEST_LIKED_PLAYLIST, create_if_missing=True)
    playlist.replace_playlist_tracks(sp, playlist_id, latest_liked_tracks_uris)


def random_liked_playlist(sp: Spotify) -> None:
    """Create a playlist with all the random liked songs.

    Args:
        sp (Spotify): Spotify object.
    """
    random_liked_tracks_uris = user_tracks.get_users_random_liked_tracks_uris(sp)
    playlist_id = playlist.get_playlist_id(sp, RANDOM_LIKED_PLAYLIST, create_if_missing=True)
    playlist.replace_playlist_tracks(sp, playlist_id, random_liked_tracks_uris)


def new_albums_playlist(sp: Spotify) -> None:
    """Create a playlist with all the new albums based on release radar.

    Args:
        sp (Spotify): Spotify object.
    """
    release_radar_playlist_id = playlist.get_playlist_id(sp, RELEASE_RADAR_PLAYLIST)
    all_artists_ids = playlist.get_artists_ids_in_playlist(sp, release_radar_playlist_id, filter_liked=True)
    all_albums_tracks = []
    for artist_id in all_artists_ids:
        latest_album_id = get_latest_artist_album_id(sp, artist_id)
        latest_album_track_uris = get_tracks_uris_in_album(sp, latest_album_id)
        all_albums_tracks.extend(latest_album_track_uris)

    playlist_id = playlist.get_playlist_id(sp, NEW_ALBUMS_PLAYLIST, create_if_missing=True)
    playlist.add_tracks_to_playlist(sp, playlist_id, all_albums_tracks)
