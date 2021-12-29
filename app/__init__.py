from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask import render_template

app = Flask(__name__, template_folder='template')
app.config.from_object(Config)

#database object
db = SQLAlchemy(app)
migrate = Migrate(app, db)


from app import routes, models