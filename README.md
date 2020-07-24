# Musical Geography
#### Exploring Associations Between Geographic and Musical Characteristics


### [Project Proposal](docs/proposal.md)

## Contents
1. [Background](#Background)

2. [Data](#Data)
    - [Acquisition](#Acquisition)
        - [Spotify](#Spotify)
        - [MusicBrainz](#MusicBrainz)
        - [ArcGIS Hub](#ArcGIS-Hub)
        - [Worldbank](#Worldbank)
    - [Exploration](#Exploration)
    - [Cleaning/Organization](#Cleaning/Organization)
    
3. [Analysis](#Analysis)
    - [Spotify Metrics](#Spotify-Metrics)
    - [Artist Birthplace](#Artist-Birthplace)
    - [Choice of Compelling Metrics](#Choice-of-Compelling-Metrics)
    
4. [Discussion](#Discussion)
    - [Conclusion](#Conclusion)
    - [Notes](#Notes)
    - [Future Plans](#Future-Plans)

5. [Resources/Reference](#Resources/Reference)

# Background
### How does someone's life experience affect their music?
Many factors in a person's life might influence what kind of music they create, but many are subjective and difficult to find (like individual personal factors/experiences/feelings).
For this exploratory analysis a few ubiquitous factors were chosen for a zoomed-out view of the relationship between personal situation and musical attributes.

[Back to top](#Contents)
# Data
Data sources: Spotify API (musical data), MusicBrainz API (artist data), ArcGIS Hub (shapefiles), Worldbank (geographic microdata), and Github (country codes).
## Acquisition
### Spotify
Based on the project proposal the original plan was to build a Python wrapper for Spotify's API in order to perform specific granular requests, but this was later abandoned as unnecessary as a 3rd party API wrapper for Python already exists ([Spotipy](https://github.com/plamere/spotipy)).
### MusicBrainz
MusicBrainz is an open database of aggregated music metadata, and was needed because Spotify doesn't store any personal information about each artist. For this project MusicBrainz' Python API wrapper [MusicBrainzngs](https://pypi.org/project/musicbrainzngs/) was used to search for each artist's name and get the birth country from the top result. 
### ArcGIS Hub
Originally a world countries shapefile from ArcGIS Hub was used for generating maps, but later in the project was replaced with Geopandas in-built `naturalearth_lowres` dataset for simplicty.
### Worldbank
The project proposal included plans to source geographic microdata (population, education, health indicators, income, etc.) from Worldbank, but this was removed from the scope due to time constraints.

<br>

[Back to top](#Contents)

## Exploration

After the Spotify dataset was read into a pandas DataFrame, the distribution of each numerical column was plotted:
![](https://github.com/wkosmos/MusicalGeography/images/)


## Cleaning/Organization
checking if any artists were outliers in num of songs or on other metrics

[Back to top](#Contents)
# Analysis

## Spotify Metrics
spotify metrics by genre
testing intuition of energy, danceability, valence:
energy vs tempo, loudness
danceability vs tempo, loudness, 
valence vs tempo, loudness
energy, valence, danceability vs each other


## Artist Birthplace

## Choice of compelling metrics

# Discussion

## Conclusion

## Notes

## Future Plans


## Resources/References
Data used in this analysis were sourced from:
**[Spotify API](https://gstudents.slack.com/archives/G015L65AESW/p1595461894242200)**
- Musical data - tempo, popularity, acousticness, danceability, energy, instrumentalness, loudness, liveness, speechiness, valence

<br>

**[MusicBrainz API](https://python-musicbrainzngs.readthedocs.io/en/v0.7.1/)**
- Artist birthplace

<br>

**[COUNTRY CODES]**(https://gist.github.com/tadast/8827699)
