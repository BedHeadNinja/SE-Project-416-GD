from flask import render_template, flash, redirect, url_for
from flask_login import current_user, login_user, login_required
import sqlalchemy as sa

#! Local Imports!#
from IMS import app, db
from IMS.models import User
from IMS.forms import LoginForm

"""                                               """
#                  Module - Routes.py               #
#   This module handles the routing of all pages in #
#   the application.                                #
#                                                   #
"""                                               """

# Routes

"""
#   Function: Index
#   Index page routing
"""
@app.route('/')
@app.route('/index')
@login_required
def index():
    return render_template('index.html',title='PLACEHOLDER')

"""
#               Function: loginID
# - Handles the first stage of the login process.
#   Gets the user's ID and verifys that it exits in
#   the database.
# - Redirects the user to registerPassword if there
#   is no password associated with the given valid ID.
#
"""
@app.route('/auth/ID', methods=['GET','POST'])
def loginID():
    # If the user is already logged in, redirect to index
    if current_user.is_authenticated:
        return redirect(url_for('index'))

    # Use the login form
    form = LoginForm()

    # If the user entered a username, post it
    if form.validate_on_submit():
        # Search database for input username
        user = db.session.scalar(
            sa.select(User).where(User.name == form.username.data))
        if user is None:
            flash('Invalid ID')
            return redirect(url_for('loginID'))
        # Remember the user
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('index'))

    return render_template('/auth/ID.html',title='Login', form=form)


"""
#   Function: logout
#   Handles user logouts
"""
@app.route('/logout')
def logout():
    # Use Flask-Login to log out the user, and return to index
    logout_user()
    return redirect(url_for('loginID'))
