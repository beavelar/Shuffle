class Request:
    def __init__(self, chart, region):
        self.chart = chart
        self.region = region

    def getChart(self):
        return self.chart

    def getRegion(self):
        return self.region