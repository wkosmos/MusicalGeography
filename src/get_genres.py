import requests
import json

url = 'https://api.spotify.com/v1/recommendations/available-genre-seeds'

if __name__ == "__main__":
    """Gets up-to-date list of existing genres from Spotify API and saves to data/genres.json."""
    response = requests.get(url)





'''curl -X "GET" "https://api.spotify.com/v1/recommendations/available-genre-seeds" -H "Accept: application/json" -H "Content-Type: application/json" -H "Authorization: Bearer BQCHC6aT5sSFZw86YLfEZqDLBzoJ-Mm9akbeXdTRYv-1bnmyNLfN1GqWUaE6rX1Bq7zYAlb0quYr6tdvlVKrHAUfIUC13sxGiY0YYsN0PtZ2iXbZNzCpP3sVGzhW4eBwBSiit4-gK5QAUfc9-FgBf8dx2OtiqG7n7JY"'''