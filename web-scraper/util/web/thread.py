import threading
from util.spotify.spotify_util import getTop200List

class Thread(threading.Thread):
    '''
    Thread class used to conduct the multi-threaded requests

    ...

    Attributes
    ----------
    name : str

    chart : str

    region : str

    songs : [Song]

    ...

    Methods
    -------
    run() : Execution of the thread
    '''

    def __init__(self, name, chart, region, songs):
        threading.Thread.__init__(self)
        self.name = name
        self.chart = chart
        self.region = region
        self.songs = songs

    def run(self):
        self.songs.append(getTop200List(self.chart, self.region))