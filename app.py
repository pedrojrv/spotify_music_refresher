"""FastAPI app entry point for the Spotify Refresher API."""
from fastapi import FastAPI

from pydantic import BaseModel
from spotify_refresher import refresh


app = FastAPI()


@app.get("/")
async def root():
    """Root endpoint."""
    return {"message": "Spotify Refresher API is running!"}


class User(BaseModel):
    """User model."""
    username: str
    password: str


@app.post("/users/register")
async def register_user(user: User) ->