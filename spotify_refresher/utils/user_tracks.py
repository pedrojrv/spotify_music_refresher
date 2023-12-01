import random

from spotipy import Spotify


def get_total_liked_songs(sp: Spotify) -> int:
    """Get the total number of liked songs.

    Args:
        sp (Spotify): Spotify object.

    Returns:
        int: Total number of liked songs.
    """
    return sp.current_user_saved_tracks(limit=1)['total']


def get_users_latest_liked_tracks_uris(sp: Spotify, num_tracks=200) -> list:
    """Get the user's latest liked tracks (uris).

    Args:
        sp (Spotify): Spotify object.
        num_tracks (int, optional): Number of tracks to get. Defaults to 200.

    Returns:
        list: List of tracks (uris).
    """
    tracks_uris = []
    offset = 0
    while True:
        response = sp.current_user_saved_tracks(limit=50, offset=offset)
        sp.user
        tracks = response['items']
        for track in tracks:
            tracks_uris.append(track['track']['uri'])
        offset += len(tracks)
        if len(tracks) == 0 or len(tracks_uris) >= num_tracks:
            break
    return tracks_uris[:num_tracks]


def get_users_random_liked_tracks_uris(sp: Spotify, num_tracks=200) -> list:
    """Get the user's random liked tracks (uris).

    Args:
        sp (Spotify): Spotify object.
        num_tracks (int, optional): Number of random tracks to get. Defaults to 200.

    Returns:
        list: List of tracks (uris).
    """
    total_number_of_tracks = get_total_liked_songs(sp)
    random_tracks_uris = []
    for _ in range(num_tracks):
        random_offset = random.randint(0, total_number_of_tracks)
        random_track = sp.current_user_saved_tracks(limit=1, offset=random_offset)['items'][0]
        random_track_uri = random_track['track']['uri']
        random_tracks_uris.append(random_track_uri)
    return random_tracks_uris
