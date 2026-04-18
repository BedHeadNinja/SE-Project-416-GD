from flask import Blueprint

bp = Blueprint('errors', __name__)

from IMS.errors import handlers
