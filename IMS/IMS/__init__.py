from flask import Flask
from .config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

# Define extension objects
# db: SQLAlchemy. Handles database
db = SQLAlchemy()
# migrate: flask-migrate. Handles database migrations
migrate = Migrate()
# login: flask-login. Handles login features like remember me. Functions with RBAC
login = LoginManager()
login.login_view = 'auth.loginID'

def create_app(config_class=Config):
    # Create flask object
    app = Flask(__name__)
    # Use configuration file
    app.config.from_object(config_class)

    # Initialize extension objects
    db.init_app(app)
    migrate.init_app(app, db)
    login.init_app(app)

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

    return app

# Import routes, models and #!REMOVED! errors
#from IMS import routes, models

# Create flask object
#app = Flask(__name__)

# Use configuration file config.py
#app.config.from_object(Config)

#Create database object
#db = SQLAlchemy(app)

# Create database migration object
#migrate = Migrate(app, db)

# Create login manager object, and set loginID as the view function that handles logins
#login = LoginManager(app)
#login.login_view = 'loginID'

##
