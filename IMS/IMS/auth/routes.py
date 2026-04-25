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

    # If the user entered a username, post it
    if form.validate_on_submit():
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
            session['user_id'] = user_input['id']
            
            if user.password_hash is None:
                return redirect(url_for('auth.registerPassword'))
            # Set the user's id as a session value
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

    # If the user entered a password, post it
    if form.validate_on_submit():
        # If the given password doesn't match the user, print an error message and repeat page
        if not user.check_password(form.password.data):
            flash('Invalid Password')
            return redirect(url_for('auth.loginPassword'))
        else:
            # Remember the user
            login_user(user, remember=form.remember_me.data)
            return redirect(url_for('main.index'))

    return render_template('/auth/password.html', title='Login', form=form)

@bp.route('/register', methods = ['GET', 'POST'])
def registerPassword():

    user = db.session.scalar(
        sa.select(User).where(User.id == session.get('user_id')))
    
    form = RegisterForm()

    if form.validate_on_submit():
        newPass = form.password.data

        user.set_password(newPass)

        db.session.merge(user)
        db.session.commit()

        flash("Password Registered!")

        return redirect('ID')
    
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
