class Song:
    '''
    Songs class used to store the song information to be sent to the bot

    ...

    Attributes
    ----------
    region : str
    
    title : str
    
    views : number
    
    videos : number

    ...

    Methods
    -------
    generateTopSongReport() -> str : Helper function to generate a simple report with simple markdown features
    '''

    def __init__(self, title, artist, views, videos):
        self.title = title
        self.artist = artist
        self.views = views
        self.videos = videos

#########################################################################################################
    
    def generateTopSongReport(self) -> str:
        '''Helper function to generate a simple report with simple markdown features'''

        heading = '**Current Top TikTok Song**\n'
        song = 'Song Title: ' + self.title + '\n'
        artist = 'Artist: ' + self.artist + '\n'
        views = 'Number of views: ' + self.views + '\n'
        videos = 'Number of popular videos: ' + self.videos
        return heading + song + artist + views + videos