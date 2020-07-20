import requests
import json
import time
import client_secret as creds

client_id = '0348c48a8fc8444eb4c88fa5601629b2'

client_secret = creds.client_secret

grant_type = 'client_credentials'



def get_multiple_tracks(ids):
    """Send GET request to https://api.spotify.com/v1/tracks """
