from flask import Blueprint

bp = Blueprint('management', __name__)

from IMS.management import routes, forms
