from flask import Blueprint

bp = Blueprint('inventory', __name__)

from IMS.inventory import routes, forms
