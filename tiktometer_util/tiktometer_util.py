import requests
from bs4 import BeautifulSoup

from tiktometer_util.Song import *

#########################################################################################################
# Retrieves the current top song from TikTok using TikTometer
#
# Returns: Song Object

def getTopTikTokSong():
    requestUrl = 'https://tiktometer.com/'
    
    response = requests.get(requestUrl)
    responseParsed = BeautifulSoup(response.text, 'html.parser')

    topChartElement = responseParsed.findAll('li')[3]
    artist = topChartElement.contents[2].contents[0]
    songName = topChartElement.contents[3].contents[0].contents[0]
    
    info = topChartElement.contents[4]
    views = info.contents[2].contents[0]
    videos = info.contents[4].contents[0]

    return Song(songName, artist, views, videos)