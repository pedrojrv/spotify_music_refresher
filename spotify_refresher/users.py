"""Utilities to sign up or remove a user."""


def user_exists(username: str) -> bool:
    """Check if a user exists in the database.

    Args:
        username (str): The username to check.

    Returns:
        bool: True if the user exists, False otherwise.
    """
    pass


def delete_user(username: str) -> None:
    """Delete a user from the database.

    Args:
        username (str): The username to delete.
    """
    pass


def create_user(username: str, password: str) -> None:
    """Create a user in the database.

    Args:
        username (str): The username to create.
        password (str): The password to create.
    """
    pass


def signin(username: str, password: str) -> None:
    """Sign in a user.

    Args:
        username (str): The username to sign in.
        password (str): The password to sign in.
    """
    pass
