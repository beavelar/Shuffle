import threading
from util.spotify.spotify_util import getTop200List

class Thread(threading.Thread):
    def __init__(self, name, chart, region, songs):
        threading.Thread.__init__(self)
        self.name = name
        self.chart = chart
        self.region = region
        self.songs = songs

    def run(self):
        self.songs.append(getTop200List(self.chart, self.region))