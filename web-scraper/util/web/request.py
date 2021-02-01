class Request:
    '''
    Request class used to store the request information to be made

    ...

    Attributes
    ----------
    chart : str

    region : str

    ...

    Methods
    -------
    getChart() : Returns the chart of the instance
    
    getRegion() : Returns the region of the instance
    '''
    
    def __init__(self, chart, region):
        self.chart = chart
        self.region = region

    def getChart(self) -> str:
        return self.chart

    def getRegion(self) -> str:
        return self.region