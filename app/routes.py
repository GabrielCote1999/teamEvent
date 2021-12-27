from flask import Flask 
from app import app

app = Flask(__name__)

#Decorator modifies the function that follows it
#It creates an association between the url (arg) and the function
@app.route('/')
def index():
    return "Hello, World!"