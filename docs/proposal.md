# Project Proposal

### How do Spotify's metrics correlate with geographic data?
Spotify stores a wide variety of data on its content, including both simple and complex categories of analysis.  
Most attributes of a track Spotify stores are expected measurable quantities/qualities of music like `duration_ms`, `key`, `loudness`, `tempo`, `mode` etc., but they also generate some intriguingly vague subjective measurements. 
<br>
<br>
These subjective attributes fall mostly into two categories: 
- Contextual information about the music and assessment of its instrumentation:
  - **acousticness** - a confidence measure of whether the track is acoustic.
  - **instrumentalness** - predicts whether a track contains no vocals. 
  - **liveness** - detects the presence of an audience in the recording. 
  - **speechiness** - detects the presence of spoken words in a track. 
- Perceptual/emotional/mood measures:
  - **energy** - a perceptual measure of intensity and activity.
  - **danceability** - how suitable a track is for dancing based on a combination of musical elements including tempo, rhythm stability, beat strength, and overall regularity.
  - **valence** - describes the musical positiveness conveyed by a track.

<br>

This project aims to better understand these subjective measurements by exploring their relationships with with objective data, both musical data from Spotify's API (eg loudness, tempo, genre, popularity) and geographic data from external sources (eg population, terrain, climate, health, income, politics).

## Data Sources, Formats, Quality
_note: Other than Spotify, these are potential sources I'm evaluating - not suggesting I use all of them_

#### [Spotify API](https://developer.spotify.com/documentation/web-api/reference-beta/)
**Type:** musical attributes\
**Access:** GET requests (via python `requests`)\
**Format:** JSON, single-layer dict\
**Quality:** Clean. Beautiful.\

<br>

#### [Worldbank](https://data.worldbank.org/)
**Type:** GIS, microdata\
**Access:** file download or API (but not sure API will be necessary for accessing single specific datasets\
**Format:** CSV, XML\
**Quality:** microdata seems pretty complete - I checked a few randomly selected indicators like population, life expectancy, literacy, etc.. \ 

<br>

#### [SEDAC](https://sedac.ciesin.columbia.edu/data/sets/browse)
**Type:** geographic, demographic\
**Access:** file download\
**Format:** XML, HTML, TXT\
**Quality:** various, but most datasets include quality metadata\

<br>

#### [IPUMS TERRA](https://terra.ipums.org/)
**Type:** demographic\
**Access:** file download\
**Format:** CSV, TXT\
**Quality:** very complete - mostly census data\

<br>

#### [ArcGIS Hub](https://hub.arcgis.com/)
**Type:** GIS shapefiles\
**Access:** file download\
**Format:** SHP (ZIP)\
**Quality:** haven't checked yet because I haven't dove into `geopandas` yet\

<br>

#### [Global Map archive](https://globalmaps.github.io/)
**Type:** geographic - elevation, land cover, tree cover\
**Access:** file download (or git I guess)\
**Format:** GeoTIFF - TIF (ZIP)\
**Quality:** haven't checked yet, re: `geopandas`\

<br>

## MVP:
- Some plots of correlations between Spotify's objective and subjective attributes, some insights/conclusions about how intuitive the subjective measures are, and how much they vary by genre
- Comparison of at least one of Spotify's subjective attributes (eg danceability) with at least one geographic attribute (eg population), by at least one objective musical attribute (eg artist/genre country of origin).

