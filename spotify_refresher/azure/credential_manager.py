"""Utilities to get credentials from azure."""
from azure.identity import DefaultAzureCredential, TokenCachePersistenceOptions
from azure.cosmos import CosmosClient

from spotify_refresher import env


ENDPOINT = env._get_cosmos_endpoint()
DATABASE_NAME = env._get_cosmos_database_name()


def _get_token_cache() -> TokenCachePersistenceOptions:
    """Get the token cache.

    Returns:
        TokenCachePersistenceOptions: The token cache.
    """
    return TokenCachePersistenceOptions(allow_unencrypted_storage=True)


def get_credential(cache: TokenCachePersistenceOptions) -> DefaultAzureCredential:
    """Get a credential from azure.

    Returns:
        DefaultAzureCredential: A credential from azure.
    """
    return DefaultAzureCredential(token_cache_persistence_options=cache)


def get_cosmodb_client(credential: DefaultAzureCredential) -> CosmosClient:
    """Get a Cosmos DB client.

    Returns:
        cosmos_client.CosmosClient: A Cosmos DB client.
    """
    return CosmosClient(url=ENDPOINT, credential=credential)
