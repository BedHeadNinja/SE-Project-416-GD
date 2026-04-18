from flask import Blueprint

bp = Blueprint('auth', __name__)

from IMS.auth import routes, forms
