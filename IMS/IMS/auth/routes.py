import time, math
from datetime import datetime, timedelta
from flask import current_app, render_template, flash, redirect, url_for, session
from flask_login import current_user, login_user, logout_user, login_required
import sqlalchemy as sa

#! Local Imports !#
from IMS import db
from IMS.auth import bp
from IMS.models import User
from IMS.auth.forms import IDForm, PasswordForm, RegisterForm

"""
#               Function: loginID
# - Handles the first stage of the login process.
#   Gets the user's ID and verifies that it exists in
#   the database.
# - Redirects the user to registerPassword if there
#   is no password associated with the given valid ID.
#
"""

@bp.route('/ID', methods=['GET','POST'])
def loginID():
    # If the user is already logged in, redirect to index
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))

    # Use the ID form
    form = IDForm()

    # Create lockout variable
    lockout = None

    if session.get('login_lockout_time'):
            if((time.time() - session['login_lockout_time']) < 300):
                lockout = True
            else:
                lockout = False

    # If the user entered a username, post it
    if form.validate_on_submit():
        if lockout:
            flash(f"You have reached the maximum number of login attempts.\nPlease try again in {math.ceil((5 - (time.time() - session['login_lockout_time'])/60))} minutes")
            return redirect(url_for('auth.loginID'))
        else:
            # Clear the active session
            session.clear()
            # Get the input username, and store it as a dict for use in "session" object
            user_input = {'id':form.username.data}
            # Search the database for id matching the user's input
            user = db.session.scalar(
                sa.select(User).where(User.id == user_input['id']))
            # If user isn't found, print an error message and repeat page
            if user is None:
                flash('Invalid ID')
                return redirect(url_for('auth.loginID'))
            else:
                # Set the user's id as a session value
                session['user_id'] = user_input['id']
                # If the user hasn't registered a password yet, redirect them to the respective page
                if user.password_hash is None:
                    return redirect(url_for('auth.registerPassword'))
                else:
                    return redirect(url_for('auth.loginPassword'))

    return render_template('/auth/ID.html',title='Login', form=form)


"""
#               Function: loginPassword
# - Handles the second stage of the login process.
#   Gets the user's password and verifies that it exists
#   in the database.
# - Redirects the user to index if the password exists
#
"""

@bp.route('/password',methods=['GET','POST'])
def loginPassword():

    # Get the correct user using the user_id session value
    user = db.session.scalar(
        sa.select(User).where(User.id == session.get('user_id')))

    # Use the password form
    form = PasswordForm()

    # Record login attempts
    if not session.get('login_attempts'):
        session['login_attempts'] = 0

    # If the user entered a password, validate it
    if form.validate_on_submit():
        # If the given password doesn't match the user, print an error message,
        # increment login attempts and repeat page
        if not user.check_password(form.password.data):
            if (session['login_attempts'] < 2):
                flash('Invalid Password')
                session['login_attempts'] += 1
                return redirect(url_for('auth.loginPassword'))
            else:
                session.clear()
                session['login_lockout_time'] = time.time()
                return redirect(url_for('auth.loginID'))
        else:
            # Remember the user
            login_user(user, remember=form.remember_me.data)
            return redirect(url_for('main.index'))

    return render_template('/auth/password.html', title='Login', form=form)

@bp.route('/register', methods = ['GET', 'POST'])
def registerPassword():

    # Get the correct user using the user_id session value
    user = db.session.scalar(
        sa.select(User).where(User.id == session.get('user_id')))

    # Create form object
    form = RegisterForm()

    # If the user entered a password, save it to the database
    if form.validate_on_submit():
        # Get new password
        newPass = form.password.data
        # Set user's password to new password
        user.set_password(newPass)
        # Update the database
        db.session.merge(user)
        db.session.commit()
        # Print a message to notify the user
        flash("Password Registered!")
        return redirect(url_for('auth.loginID'))

    return render_template('/auth/register.html',title='Login', form=form)




"""
#   Function: logout
#   Handles user logouts
"""
@bp.route('/logout')
def logout():
    # Use Flask-Login to log out the user, and return to index
    logout_user()
    return redirect(url_for('auth.loginID'))
