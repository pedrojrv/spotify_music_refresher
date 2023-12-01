from spotipy import Spotify


def get_all_artist_albums_ids(sp: Spotify, artist_id: str, sort_by_date=True) -> list:
    """Get all the albums ids from an artist.

    Args:
        sp (Spotify): Spotify object.
        artist_id (str): Artist ID.
        sort_by_date (bool, optional): Sort by date. Defaults to True.

    Returns:
        list: List of album IDs.
    """
    all_albums = []
    offset = 0
    while True:
        albums = sp.artist_albums(artist_id, limit=50, offset=offset, album_type='album,single')
        for album in albums['items']:
            all_albums.append(album)
        offset += len(albums['items'])
        if len(albums['items']) == 0:
            break

    if sort_by_date:
        all_albums.sort(key=lambda album: album['release_date'], reverse=True)

    return [album['id'] for album in all_albums]


def get_latest_artist_album_id(sp: Spotify, artist_id: str) -> str:
    """Get the latest album id from an artist.

    Args:
        sp (Spotify): Spotify object.
        artist_id (str): Artist ID.

    Returns:
        str: Album ID.
    """
    # sorting is not supported and artist_albums returns unsorted results
    albums = get_all_artist_albums_ids(sp, artist_id)
    return albums[0]
