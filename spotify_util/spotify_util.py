import requests
from bs4 import BeautifulSoup

from spotify_util.Song import *

#########################################################################################################
# Retrieves the top song from Spotify charts provided the region
#
# Parameters
# urlExt: string
# region: string
# regionHeading: string
#
# Returns: Song Object

def getTopSong(urlExt, region, regionHeading):
    top200 = getTop200List(region, regionHeading)

    return top200[0]

#########################################################################################################
# Retrieves a list of the top 200 songs from Spotify charts provided the region
#
# Parameters
# urlExt: string
# region: string
# regionHeading: string
#
# Returns: List of Song Objects

def getTop200List(urlExt, region, regionHeading):
    songs = []
    artists = []
    streams = []
    
    spotifyChartsUrl = 'https://spotifycharts.com/' + urlExt + '/'
    requestUrl = spotifyChartsUrl + region + '/daily/latest'
    
    response = requests.get(requestUrl)
    responseParsed = BeautifulSoup(response.text, 'html.parser')

    chartElements = responseParsed.findAll('tr')

    for chartElement in chartElements:
        if len(chartElement.contents) > 8:
            song = chartElement.contents[7].contents[1].contents[0]
            artist = chartElement.contents[7].contents[3].contents[0][3:]

            if len(chartElement.contents) == 11:
                streams = chartElement.contents[9].contents[0]
                songs.append(Song(regionHeading, song, artist, streams))
            else:
                songs.append(Song(regionHeading, song, artist, 'N/A'))

    return songs