

class EventCatalog:
    def __init__(self, event: list):
        self.event = event

    def getEvent(self):
        return self.event
    
    def setEvent(self, event):
        self.event.append(event)

        