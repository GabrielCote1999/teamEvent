from datetime import date
class User:
    def __init__(self, firstName: str, lastName: str, password: str, adress: str, email: str, role: str):
        self.firstName = firstName
        self.lastName = lastName
        self.password = password
        self.adress = adress
        self.email = email
        self.creationDate = date.today()
        self.role = role
        self.event = []

    def getFirstName(self):
        return self.firstName

    def setFirstName(self,firstName: str):
        self.firstName = firstName
    
    def getLastName(self):
        return self.lastName

    def setLastName(self, lastName: str):
        self.lastName = lastName

    def getPassword(self):
        return self.password
    
    def setPassword(self, password: str):
        self.password = password

    def getAdress(self):
        return self.adress

    def setAdress(self,adress: str):
        self.adress = adress
    
    def getEmail(self):
        return self.email

    def setEmail(self, email: str):
        self.email = email
    
    def getCreationDate(self):
        return self.creationDate.strftime("%d/%m/%Y")

    def setCreationDate(self, dates):
        self.getCreationDate = date
