from flask import render_template, flash, redirect, url_for, session
from flask_login import current_user, login_user, logout_user, login_required
from IMS.main import bp
"""
#   Function: Index
#   Index page routing
"""
@bp.route('/')
@bp.route('/index')
@login_required
def index():
    return render_template('index.html',title='Home - IMS')
