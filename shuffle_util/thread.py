import requests
import threading

from bs4 import BeautifulSoup
from spotify_util.Song import *
from spotify_util.spotify_util import *

class Thread(threading.Thread):
    def __init__(self, name, chart, region, songs):
        threading.Thread.__init__(self)
        self.name = name
        self.chart = chart
        self.region = region
        self.songs = songs

    def run(self):
        self.songs.append(getTop200List(self.chart, self.region))