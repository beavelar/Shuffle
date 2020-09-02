class Song:
    # __init__ - Constructor
    #
    # Parameters:
    # region: string
    # title: string
    # streams: string

    def __init__(self, region, title, artist, streams):
        self.region = region
        self.title = title
        self.artist = artist
        self.streams = streams

#########################################################################################################
    # generateTopSongReport - Helper function to generate a simple report with simple markdown features
    #
    # Returns: string
    
    def generateTopSongReport(self):
        heading = '**' + self.region + '**\n'
        title = 'Top Song: ' + self.title + '\n'
        artist = 'Artist: ' + self.artist + '\n'
        streams = 'Number of Spotify Streams: ' + self.streams

        return heading + title + artist + streams

#########################################################################################################
    # generateRandomSongReport - Helper function to generate a simple report with simple markdown features
    #
    # Returns: string
    
    def generateRandomSongReport(self):
        heading = '**Random Song**\n'
        title = 'Song: ' + self.title + '\n'
        artist = 'Artist: ' + self.artist + '\n'

        if 'N/A' in self.streams:
            streams = 'Number of Spotify Streams: ' + self.streams
            return heading + title + artist + streams
        else:
            return heading + title + artist