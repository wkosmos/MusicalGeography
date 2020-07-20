import requests
import json

url = 'https://api.spotify.com/v1/recommendations/available-genre-seeds'

if __name__ == "__main__":
    """Gets up-to-date list of existing genres from Spotify API and saves to data/genres.json."""
    response = requests.get(url)