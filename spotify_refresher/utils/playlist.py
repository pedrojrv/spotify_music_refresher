from spotipy import Spotify

from spotify_refresher.utils.tracks import check_if_user_likes_track


def get_playlist_id(sp: Spotify, playlist_name: str, create_if_missing=False) -> str:
    """Get the playlist id from a playlist name.

    Args:
        sp (Spotify): Spotify object.
        playlist_name (str): Playlist name.

    Returns:
        str: Playlist ID.
    """
    playlists = sp.current_user_playlists()
    for playlist in playlists['items']:
        if playlist['name'] == playlist_name:
            return playlist['id']

    if create_if_missing:
        sp.user_playlist_create(sp.me()['id'], playlist_name, public=False)
        return get_playlist_id(sp, playlist_name, create_if_missing=False)
    return None


def get_playlist_tracks_uris(sp: Spotify, playlist_id: str) -> list:
    """Get all the tracks (uris) from a playlist.

    Args:
        sp (Spotify): Spotify object.
        playlist_id (str): Playlist ID.

    Returns:
        list: List of tracks (uris).
    """
    tracks_uris = []
    offset = 0
    while True:
        response = sp.playlist_tracks(playlist_id, offset=offset)
        tracks = response['items']
        for track in tracks:
            tracks_uris.append(track['track']['uri'])
        offset += len(tracks)
        if len(tracks) == 0:
            break
    return tracks_uris


def get_total_number_of_tracks_in_playlist(sp: Spotify, playlist_id: str) -> int:
    """Get the total number of tracks in a playlist.

    Args:
        sp (Spotify): Spotify object.
        playlist_id (str): Playlist ID.

    Returns:
        int: Total number of tracks in the playlist.
    """
    response = sp.playlist_tracks(playlist_id)
    return response['total']


def get_artists_ids_in_playlist(sp: Spotify, playlist_id: str, filter_liked=False) -> list:
    """Get all the artists ids from a playlist.

    Args:
        sp (Spotify): Spotify object.
        playlist_id (str): Playlist ID.
        filter_liked (bool, optional): Filter liked tracks. Defaults to False.

    Returns:
        list: List of artists ids.
    """
    artists_ids = []
    offset = 0
    while True:
        response = sp.playlist_tracks(playlist_id, offset=offset)
        tracks = response['items']
        for track in tracks:
            if filter_liked and not check_if_user_likes_track(sp, track['track']['id']):
                continue

            for artist in track['track']['artists']:
                artists_ids.append(artist['id'])
        offset += len(tracks)
        if len(tracks) == 0:
            break
    return artists_ids


def empty_playlist(sp: Spotify, playlist_id: str) -> None:
    """Empty a playlist.

    Args:
        sp (Spotify): Spotify object.
        playlist_id (str): Playlist ID.
    """
    tracks_uris = get_playlist_tracks_uris(sp, playlist_id)
    # web api only allows 100 tracks to be removed at a time
    for i in range(0, len(tracks_uris), 100):
        sp.playlist_remove_all_occurrences_of_items(playlist_id, tracks_uris[i:i + 100])


def replace_playlist_tracks(sp: Spotify, playlist_id: str, tracks_uris: list) -> None:
    """Replace all the tracks in a playlist.

    Args:
        sp (Spotify): Spotify object.
        playlist_id (str): Playlist ID.
        tracks_uris (list): List of tracks (uris).
    """
    empty_playlist(sp, playlist_id)
    # web api only allows 100 tracks to be added at a time
    for i in range(0, len(tracks_uris), 100):
        sp.playlist_add_items(playlist_id, tracks_uris[i:i + 100])


def add_tracks_to_playlist(sp: Spotify, playlist_id: str, tracks_uris: list, add_duplicates=False) -> None:
    """Add tracks to a playlist.

    Args:
        sp (Spotify): Spotify object.
        playlist_id (str): Playlist ID.
        tracks_uris (list): List of tracks (uris).
        add_duplicates (bool, optional): Add duplicates. Defaults to False.
    """
    if add_duplicates:
        # web api only allows 100 tracks to be added at a time
        for i in range(0, len(tracks_uris), 100):
            sp.playlist_add_items(playlist_id, tracks_uris[i:i + 100])
    else:
        tracks_uris_in_playlist = set(get_playlist_tracks_uris(sp, playlist_id))
        # check if the track is already in the playlist
        tracks_uris_to_add = [track_uri for track_uri in tracks_uris if track_uri not in tracks_uris_in_playlist]
        # web api only allows 100 tracks to be added at a time
        for i in range(0, len(tracks_uris_to_add), 100):
            sp.playlist_add_items(playlist_id, tracks_uris_to_add[i:i + 100])
