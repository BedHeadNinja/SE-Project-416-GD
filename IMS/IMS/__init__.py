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

# Create errors blueprint
from IMS.errors import bp as errors_bp
app.register_blueprint(errors_bp)

# Create auth blueprint
from IMS.auth import bp as auth_bp
app.register_blueprint(auth_bp, url_prifix='/auth')

# Create inventory blueprint
from IMS.inventory import bp as inventory_bp
app.register_blueprint(inventory_bp, url_prefix='/inventory')

# Creat main blueprint
from IMS.main import bp as main_bp
app.register_blueprint(main_bp)

# Import routes, models and #!REMOVED! errors
#from IMS import routes, models
