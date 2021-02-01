class Song:
    '''
    Thread class used to conduct the multi-threaded requests

    ...

    Attributes
    ----------
    region : str
    
    title : str

    artist : str
    
    streams : str

    ...

    Methods
    -------
    generateTopSongReport() -> str : Helper function to generate a simple report with simple markdown features

    generateRandomSongReport() -> str : Helper function to generate a simple report with simple markdown features
    '''

    def __init__(self, region, title, artist, streams):
        self.region = region
        self.title = title
        self.artist = artist
        self.streams = streams

#########################################################################################################
    
    def generateTopSongReport(self) -> str:
        '''Helper function to generate a simple report with simple markdown features'''

        heading = '**' + self.region + '**\n'
        title = 'Top Song: ' + self.title + '\n'
        artist = 'Artist: ' + self.artist + '\n'
        streams = 'Number of Spotify Streams: ' + self.streams

        return heading + title + artist + streams

#########################################################################################################
    
    def generateRandomSongReport(self) -> str:
        '''Helper function to generate a simple report with simple markdown features'''

        heading = '**Random Song**\n'
        title = 'Song: ' + self.title + '\n'
        artist = 'Artist: ' + self.artist + '\n'

        if 'N/A' in self.streams:
            streams = 'Number of Spotify Streams: ' + self.streams
            return heading + title + artist + streams
        else:
            return heading + title + artist