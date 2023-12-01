"""These are exposed to the web app and are used to enable/disable the various playlists."""


def enable_disable_top_music_playlist(username: str, enable: bool) -> None:
    """Enable the top music playlist for the user.

    Args:
        username (str): The username to enable the top music playlist for.
        enable (bool): True to enable, False to disable.
    """
    pass


def enable_disable_latest_liked_playlist(username: str, enable: bool) -> None:
    """Enable the latest liked playlist for the user.

    Args:
        username (str): The username to enable the latest liked playlist for.
        enable (bool): True to enable, False to disable.
    """
    pass


def enable_disable_random_liked_playlist(username: str, enable: bool) -> None:
    """Enable the random liked playlist for the user.

    Args:
        username (str): The username to enable the random liked playlist for.
        enable (bool): True to enable, False to disable.
    """
    pass


def enable_disable_new_albums_playlist(username: str, enable: bool) -> None:
    """Enable the new albums playlist for the user.

    Args:
        username (str): The username to enable the new albums playlist for.
        enable (bool): True to enable, False to disable.
    """
    pass


def enable_disable_nostalgia_playlist(username: str, enable: bool, nostalgia_percentage: float) -> None:
    """Enable the nostalgia playlist for the user.

    Args:
        username (str): The username to enable the nostalgia playlist for.
        enable (bool): True to enable, False to disable.
        nostalgia_percentage (float): The percentage of nostalgia to use.
    """
    pass
