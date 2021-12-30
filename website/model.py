from datetime import datetime, timezone
import datetime
from enum import unique
from werkzeug.security import generate_password_hash, check_password_hash
#from website.__init__ import login

from flask_login import UserMixin

from . import db

class User(db.Model, UserMixin):
    
    id = db.Column(db.Integer, primary_key=True)
    firstName = db.Column(db.String(64), index = True)
    lastName = db.Column(db.String(64), index = True)
    email = db.Column(db.String(64), index = True, unique= True)
    password_hash = db.Column(db.String(128))
    creationDate = db.Column(db.DateTime(timezone=True), default = datetime.datetime.utcnow())
    #list of events that a user is in
    #events = db.relationship('Event')

def setPassword(self, password):
    self.password_hash = generate_password_hash(password)

def checkPassword(self,password):
    return check_password_hash(self.pasword_hash, password)
"""
@login.user_loader
def loadUser(id):
    return User.query.get(int(id))"""

"""def init_db():
    db.create_all()
    new_user = User('jhonny', 'test','jhonny@gtest.com')
    db.session.add(new_user)
    db.session.commit()

init_db()"""

class Event(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    adress = db.Column(db.String, index = True)
    #reference the category table TODO
    #categoryId = db.Column(db.Integer, db.ForeignKey('category.id'))
    name = db.Column(db.String(64))
    startDate = db.Column(db.DateTime(timezone=True))
    endDate = db.Column(db.DateTime(timezone=True))
    creationDate = db.Column(db.DateTime(timezone=True), default = datetime.datetime.utcnow())
    vote = db.Column(db.Integer())




