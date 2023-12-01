from spotipy import Spotify


def get_tracks_uris_in_album(sp: Spotify, album_id: str) -> list:
    """Get all the tracks (uris) from an album.

    Args:
        sp (Spotify): Spotify object.
        album_id (str): Album ID.

    Returns:
        list: List of tracks (uris).
    """
    tracks_uris = []
    offset = 0
    while True:
        response = sp.album_tracks(album_id, offset=offset)
        tracks = response['items']
        for track in tracks:
            tracks_uris.append(track['uri'])
        offset += len(tracks)
        if len(tracks) == 0:
            break
    return tracks_uris
