class Song:
    # __init__ - Constructor
    #
    # Parameters:
    # region: string
    # title: string
    # streams: string

    def __init__(self, region, title, streams):
        self.region = region
        self.title = title
        self.streams = streams

#########################################################################################################
    # generateReport - Helper function to generate a simple report with simple markdown features
    #
    # Parameters
    # titleReportPrefix: string
    #
    # Returns: string
    
    def generateReport(self, titleReportPrefix):
        regionReport = '**' + self.region + '**\n'
        titleReport = titleReportPrefix + ': ' + self.title + '\n'
        streamsReport = 'Number of spotify streams: ' + self.streams

        return regionReport + titleReport + streamsReport