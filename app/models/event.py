class Event:
    def __init__(self, startingDate: str, endDate: str, name: str, location: str):
        self.startingDate = startingDate
        self.endDate = endDate
        self.name = name
        self.location = location
        self.user = []

    def setStartingDate(self, date):
        self.startingDate = date

    def getStartingDate(self):
        return self.startingDate

    def setEndDate(self, endDate):
        self.endDate = endDate
    
    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name
    
    def getLocation(self,location):
        return self.location

    def setLocation(self, location):
        self.location = location


    