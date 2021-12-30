from flask import Flask

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Config, Migrate
from flask import render_template
import os
from os import path
from flask_login import LoginManager


db = SQLAlchemy()
DB_NAME = 'database.db'



def create_app():

    app = Flask(__name__, template_folder='template')
    #login = LoginManager(app)
    app.config['SECRET_KEY'] = 'thisIsMySecretKey'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)
  
    #database object
    
    app.config.from_object(Config)
    migrate = Migrate(app, db)
    from .views import views


    app.register_blueprint(views, url_prefix = '/')

    from .model import User, Event
    
    createDatabase(app)

    

    return app

def createDatabase(app):
    if not path.exists('website/' +DB_NAME):
        db.create_all(app=app)
        print('database is created')

