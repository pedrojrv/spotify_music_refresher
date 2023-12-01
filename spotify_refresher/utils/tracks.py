from spotipy import Spotify


def check_if_user_likes_track(sp: Spotify, track_id: str) -> bool:
    """Check if the user likes a track.

    Args:
        sp (Spotify): Spotify object.
        track_id (str): Track id.

    Returns:
        bool: True if the user likes the track, False otherwise.
    """
    track_ids = [track_id]
    track_likes = sp.current_user_saved_tracks_contains(track_ids)
    return track_likes[0]
