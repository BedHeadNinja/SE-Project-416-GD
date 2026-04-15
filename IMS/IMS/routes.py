from flask import render_template, flash, redirect, url_for, session
from flask_login import current_user, login_user, logout_user, login_required
import sqlalchemy as sa

#! Local Imports!#
from IMS import app, db
from IMS.models import User, Product
from IMS.forms import IDForm, PasswordForm

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
#   Gets the user's ID and verifies that it exists in
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

    # Use the ID form
    form = IDForm()

    # If the user entered a username, post it
    if form.validate_on_submit():
        # Clear the active session
        session.clear()
        # Get the input username, and store it as a dict for use in "session" object
        user_input = {'id':form.username.data}
        # Search the database for id matching the user's input
        user = db.session.scalar(
            sa.select(User).where(User.id == form.username.data))
        # If password isn't found, print an error message and repeat page
        if user is None:
            flash('Invalid ID')
            return redirect(url_for('loginID'))
        else:
            # Set the user's id as a session value
            session['user_id'] = user_input['id']
            return redirect(url_for('loginPassword'))

    return render_template('/auth/ID.html',title='Login', form=form)


"""
#               Function: loginPassword
# - Handles the second stage of the login process.
#   Gets the user's password and verifies that it exists
#   in the database.
# - Redirects the user to index if the password exists
#
"""
@app.route('/auth/password',methods=['GET','POST'])
def loginPassword():

    # Get the correct user using the user_id session value
    user = db.session.scalar(
        sa.select(User).where(User.id == session.get('user_id')))

    # Use the password form
    form = PasswordForm()

    # If the user entered a password, post it
    if form.validate_on_submit():
        # If the given password doesn't match the user, print an error message and repeat page
        if not user.check_password(form.password.data):
            flash('Invalid Password')
            return redirect(url_for('loginPassword'))
        else:
            # Remember the user
            login_user(user, remember=form.remember_me.data)
            return redirect(url_for('index'))

    return render_template('/auth/password.html', title='Login', form=form)


"""
#   Function: logout
#   Handles user logouts
"""
@app.route('/logout')
def logout():
    # Use Flask-Login to log out the user, and return to index
    logout_user()
    return redirect(url_for('loginID'))


"""
#   Function: inventory
#   Handles displaying and managing inventory
#   !!INCOMPLETE!!
"""
@app.route('/inventory', methods=['GET','POST'])
@login_required
def inventory():
    #Pull product data from database
    products = db.session.query(Product.__table__).all()

    ## !!INCOMPLETE!! - UNDER CONSTRUCTION!! ##
    #if request.method =='POST':
        #if request

    return render_template('inventory.html',title='PLACEHOLDER', products=products)




