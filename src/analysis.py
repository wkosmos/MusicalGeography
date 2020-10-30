import pandas as pd
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
import seaborn as sns

import csv

import musicbrainzngs as mb
import client_secret as creds

import Levenshtein as lev


def musicbrainzngs_init(user, pw, email, reqs_per_sec=45):

    # set up musicbrainz connection
    mb.auth(user, pw)

    mb.set_useragent('python-musicbrainz/0.7.3', '0.0', email)

    mb.set_rate_limit(limit_or_interval=1.0, new_requests=reqs_per_sec)


def search_artist(name, limit=1):
    """Returns top n results for artist search.
    
    Args:
    name (str): query for search
    limit (int): num of results to request (default 1)

    Returns:
    results (json): search results as {'artist-list': [list of results {result}]}
    
    """
    return mb.search_artists(query=name, limit=limit)


def get_artist_birthplace(name, debug=False):
    """Gets artist's birth country as country code.
    
    Args:
    name (str): name of artist
    debug (bool): print debug info to terminal

    Returns:
    (tuple): name of artist found, country code
    
    """
    limit = 1 # could improve by getting 2 or 3 results and checking similarity
    result = mb.search_artists(query=name, limit=limit)
    
    
    if debug == True:
        print(name)
    
    try:
        artist = result['artist-list'][0]
        return (artist['name'], artist['country'])
    
    except KeyError as e:
        print('Exception: ', e)
        return (artist['name'], None)

    except IndexError:
        return (None, None)


def compare_query_to_result(name):
    """Compare query string and name attribute of top result using Levenshtein distance.
    
    Args:
    name (str): artist name query

    Returns:
    (int): Levenshtein distance between query and name of top result
    """
    limit = 1
    name = name.lower()
    
    result = mb.search_artists(query=name, limit=limit)
    try:
        artist = result['artist-list'][0]
        result_name = artist['name'].lower()
        lev_dist = lev.distance(result_name, name)

        return (lev_dist)
    
    except:
    
        return None

def get_all_birthplaces(in_list, filepath, debug=False):
    """Get birthplaces for all artists in input list and write to CSV.
    
    Args:
    in_list (lst): list of artist names
    filepath (str): path of csv to write to
    debug (bool): print debug to console

    No return.
    """
    birthplace_dict_list = []
    
    for i in range(len(in_list)):
        birthplace_dict = {}
        artist = in_list[i]
        response = get_artist_birthplace(artist)
        birthplace_dict['name'] = response[0]
        birthplace_dict['birth_country'] = response[1]

        birthplace_dict_list.append(birthplace_dict)

        if debug == True:
            print('Name: ', birthplace_dict['name'], '| Country: ', birthplace_dict['birth_country'])
    
    with open(filepath, 'a') as f:
        header_names = ['name', 'birth_country']
        writer = csv.DictWriter(f, fieldnames=header_names)

        writer.writeheader()

        for i in birthplace_dict_list:
            writer.writerow(i)

# def load_birthplace_csv()
        


if __name__ == "__main__":
    
    # load spotify data
    df = pd.read_csv('data/SpotifyFeatures.csv')

    # np array of artist names
    artists_array = df['artist_name'].unique()
    print(str(len(artists_array)) + ' unique artists in dataset.')

    musicbrainzngs_init(creds.mb_user, creds.mb_password, creds.contact, reqs_per_sec=40)

    # artists_list = artists_array.tolist()

    # get_all_birthplaces(artists_list, 'birthplaces.csv', debug=True)

    artist_df = pd.DataFrame(artists_array, columns=['name'])
    birthplace_df = pd.read_csv('data/birthplaces.csv')

    artist_birthplace_df = artist_df.merge(birthplace_df)

    artist_birthplace_df.info()

    artist_birthplace_df.to_csv('data/artist_birthplace.csv')

    artist_birthplace_df.info()


    # artist_df['artist_birthplace'] = birthplace_list

    # name_accuracy_list = [compare_query_to_result(artists_array[i]) for i in range(len(artists_array))]
    # name_accuracy = pd.DataFrame()

