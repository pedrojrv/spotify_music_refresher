"""Constants for the Spotify Refresher app."""
import os


def _get_cosmos_endpoint() -> str:
    """Get the cosmos endpoint.

    Returns:
        str: The cosmos endpoint.
    """
    return os.environ["COSMOS_ENDPOINT"]


def _get_cosmos_database_name() -> str:
    """Get the cosmos database name.

    Returns:
        str: The cosmos database name.
    """
    return os.environ["COSMOS_DATABASE_NAME"]
