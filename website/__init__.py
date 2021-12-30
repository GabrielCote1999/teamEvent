from flask import Flask

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask import render_template
import os
from os import path
#from website.config import Config

db = SQLAlchemy()
DB_NAME = 'database.db'



def create_app():

    app = Flask(__name__, template_folder='template')
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'thisIsMySecretKey'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)
    #database object
    #migrate = Migrate(app, db)
    from .views import views
    from website.models import model

    app.register_blueprint(views, url_prefix = '/')

    from website.models.model import User, Event
    
    createDatabase(app)

    return app

def createDatabase(app):
    if not path.exists('website/' +DB_NAME):
        db.create_all(app=app)
        print('database is crated')

