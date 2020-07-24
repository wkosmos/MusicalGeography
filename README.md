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
        - [Intuitiveness of Metrics](#Intuitiveness-of-Metrics)
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
MusicBrainz is an open database of aggregated music metadata, and was needed because Spotify doesn't store any personal information about each artist. For this project MusicBrainz' Python API wrapper [MusicBrainzngs](https://pypi.org/project/musicbrainzngs/) was used to search for each artist's name and write the birth country from the top result to a csv file.

### ArcGIS Hub
Originally a world countries shapefile from ArcGIS Hub was used for generating maps, but later in the project was replaced with Geopandas in-built `naturalearth_lowres` dataset for simplicty.
### Worldbank
The project proposal included plans to source geographic microdata (population, education, health indicators, income, etc.) from Worldbank, but this was removed from the scope due to time constraints.

<br>

[Back to top](#Contents)

## Exploration

After the Spotify dataset was read into a pandas DataFrame, the distribution of each numerical column was plotted:
![distributions of numerical columns](https://github.com/wkosmos/MusicalGeography/blob/master/images/dists%20of%20numeric%20columns.png)

_**Note:**_  <br> **Popularity**, **acousticness**, and **valence** seemed to have more extreme values than expected, possibly due to some sort of threshold in Spotify's calculation of these metrics.

### Intuitiveness of Metrics
Spotify's description of of the subjective metrics **danceability**, **energy**, and **valence** are a bit too vague to form a confident idea of what they measure, so some comparisons were necessary to gauge their intuitiveness. 

<br>

**Spotify API Docs Definitions:**

_**Danceability**  describes how suitable a track is for dancing based on a combination of musical elements including tempo, rhythm stability, beat strength, and overall regularity._

_**Energy** is a measure from 0.0 to 1.0 and represents a perceptual measure of intensity and activity. Typically, energetic tracks feel fast, loud, and noisy._

_**Valence** is measure from 0.0 to 1.0 describing the musical positiveness conveyed by a track. Tracks with high valence sound more positive (e.g. happy, cheerful, euphoric), while tracks with low valence sound more negative (e.g. sad, depressed, angry)._

<br>

First, each subjective metric was plotted against two objective metrics: **tempo** and **loudness**.

![danceability vs tempo and loudness](https://github.com/wkosmos/MusicalGeography/blob/master/images/danceability%20vs%20objectives.png)

<br>

- Spotify appeared to be treating the 100-150 bpm range as the most danceable, which is roughly intuitive if it's assumed that people don't want to dance either too slow or too fast.
- High danceability appearing to coincide with high loudness fit with the typical idea of dance music.

![energy vs tempo and loudness](https://github.com/wkosmos/MusicalGeography/blob/master/images/energy%20vs%20objectives.png)

<br>

- Energy appeared to have a very rough positive association with tempo.
- Energy had a strong positive association with loudness, which makes intuitive sense and suggests that loudness might have been used in the calculation of energy.

![valence vs tempo and loudness](https://github.com/wkosmos/MusicalGeography/blob/master/images/valence%20vs%20objectives.png)

<br>

- Valence had nearly no association with tempo or loudness other than a slightly wider range of loudness values being present at 0 and 1 valence, which was likely due to the significantly larger number of tracks with these valence values.

<br>

The three subjective metrics were also plotted against each other, and appeared to all have a rough positive association.

![danceability vs energy vs valence](https://github.com/wkosmos/MusicalGeography/blob/master/images/subjectives%20comparisons.png)

<br>

Finally, five illustrative genres were chosen and the density distribution of the three subjective metrics was plotted for each. These distributions mostly aligned with expectations of the genres.

![five genres danceability energy valence](https://github.com/wkosmos/MusicalGeography/blob/master/images/5%20genres%20subjectives.png)

<br>

[Back to top](#Contents)


## Cleaning/Organization
The Spotify dataset was very clean as acquired, though only 11 of the 18 columns were used.  
Of the 14565 unique artists in the dataset, 9141 had a birth country value found via the MusicBrainz API, so it was only these which could be included in the later analysis of music metrics by birth country.

#### Country Codes
Unfortunately, the MusicBrainz database stores country codes in the ISO Alpha-2 format (2-length string), while the geopandas `naturalearth_lowres` dataframe contains country codes only in the ISO- Alpha-3 format (3-length string).  
A csv including both ISO-a2 and ISO-a3 country codes was found on Github, and this was loaded into pandas and merged into the world dataframe.  

Once the country codes in the geopandas dataframe matched those sourced from MusicBrainz columns could be added with counts and means of columns from the Spotify dataset.


[Back to top](#Contents)
# Analysis

## 



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
