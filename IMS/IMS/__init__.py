import logging
from flask import Flask
from .config import Config
from sqlalchemy import MetaData
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
    migrate.init_app(app, db, render_as_batch=True)
    login.init_app(app)

    # Create errors blueprint
    from IMS.errors import bp as errors_bp
    app.register_blueprint(errors_bp)

    # Create auth blueprint
    from IMS.auth import bp as auth_bp
    app.register_blueprint(auth_bp, url_prefix='/auth')

    # Create inventory blueprint
    from IMS.inventory import bp as inventory_bp
    app.register_blueprint(inventory_bp, url_prefix='/inventory')

    # Creat main blueprint
    from IMS.main import bp as main_bp
    app.register_blueprint(main_bp)

    # Create management blueprint
    from IMS.management import bp as management_bp
    app.register_blueprint(management_bp, url_prefix='/management')

    return app
