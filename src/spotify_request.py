import json
import time
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import client_secret as creds

client_id = '0348c48a8fc8444eb4c88fa5601629b2'

# set up spotipy
client_credentials_manager = SpotifyClientCredentials(client_id = client_id, client_secret = creds.client_secret)

sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

headers = {'Content-Type' : 'application/json'}



def get_top_tracks_from_genre(genre: str, offset=0, limit=50):
    """Search via spotipy within specific genre.
    Args:
    
    Returns:
    """
    query = 'genre:' + genre
    response = sp.search(q=query, type='track', offset=offset, limit=limit)

    return response


def get_multiple_tracks(ids):
    """Send GET request to API via spotipy info on each track ID given.
    Args:

    Returns:

    """

    
    pass

print(get_top_tracks_from_genre('jazz'))