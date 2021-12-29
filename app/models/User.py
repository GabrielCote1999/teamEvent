from datetime import date
from enum import unique
from app import db

class User(db.Model):
    
    id = db.Column(db.Integer, primary_key=True)
    adress = db.Column(db.String, foreign_key = True)
    firstName = db.Column(db.String(64), index = True)
    lastName = db.Column(db.String(64), index = True)
    email = db.Column(db.String(64), index = True, unique= True)
    password_hash = db.Column(db.String(128))

    def __repr__(self):
        return '<User{}'.format(self.email)
       

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
