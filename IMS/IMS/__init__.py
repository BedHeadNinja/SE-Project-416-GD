from flask import Flask
#!!! NOT WORKING, OVERRIDING from .config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# Create flask object
app = Flask(__name__)

#!!! NOT WORKING, OVERRIDING
# Use configuration file config.py
#app.config.from_object

# Set database URI
app.config['SQLALCHEMY_DATABASE_URI']='postgresql+psycopg2://brandon@localhost:5432/flask_test'

#Create database object
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from IMS import routes, models
#from .routes import route
#from .models import models
