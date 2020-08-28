import requests
from bs4 import BeautifulSoup

from spotify_util.Song import *

#########################################################################################################
# Retrieves the top song from Spotify charts provided the region
#
# Parameters
# region: string
#
# Returns: Song Object

def getTopSong(region, regionHeading):
    spotifyChartsUrl = 'https://spotifycharts.com/regional/'
    requestUrl = spotifyChartsUrl + region + '/daily/latest'
    
    response = requests.get(requestUrl)
    responseParsed = BeautifulSoup(response.text, 'html.parser')

    topChartElement = responseParsed.findAll('tr')[1]

    song = topChartElement.contents[7].contents[1].contents[0]
    artist = topChartElement.contents[7].contents[3].contents[0][3:]
    streams = topChartElement.contents[9].contents[0]

    return Song(regionHeading, song, artist, streams)