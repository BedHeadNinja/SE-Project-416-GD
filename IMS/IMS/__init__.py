from flask import Flask
from .config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

# Create flask object
app = Flask(__name__)

# Use configuration file config.py
app.config.from_object(Config)

#Create database object
db = SQLAlchemy(app)

# Create database migration object
migrate = Migrate(app, db)

# Create login manager object, and set loginID as the view function that handles logins
login = LoginManager(app)
login.login_view = 'loginID'

# Import routes and models
from IMS import routes, models
