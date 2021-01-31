class Song:
    # __init__ - Constructor
    #
    # Parameters:
    # region: string
    # title: string
    # views: string
    # videos: string

    def __init__(self, title, artist, views, videos):
        self.title = title
        self.artist = artist
        self.views = views
        self.videos = videos

#########################################################################################################
    # generateTopSongReport - Helper function to generate a simple report with simple markdown features
    #
    # Parameters
    # titleReportPrefix: string
    #
    # Returns: string
    
    def generateTopSongReport(self):
        heading = '**Current Top TikTok Song**\n'
        song = 'Song Title: ' + self.title + '\n'
        artist = 'Artist: ' + self.artist + '\n'
        views = 'Number of views: ' + self.views + '\n'
        videos = 'Number of popular videos: ' + self.videos

        return heading + song + artist + views + videos