from flask import current_app, render_template, flash, redirect, url_for, session
from flask_login import current_user, login_user, logout_user, login_required
import sqlalchemy as sa

#! Local Imports!#
from IMS import db
from IMS.models import User
from IMS.management import bp
from IMS.management.forms import AddEmployeeForm, RemoveEmployeeForm


@bp.route('/management/employee_info')
@login_required
def employee_info():

    #Pull user data from database
    users = db.session.query(User.__table__).all()
    user = db.session.scalar(
            sa.select(User).where(User.id == session['user_id']))

    if user.role != 'Manager'and user.role != 'manager':
        flash("You do not have access to this page!")
        return redirect('/index')

    addEmployeeForm = AddEmployeeForm()
    removeEmployeeForm = RemoveEmployeeForm()

    userStats = [len(users), 0, 0]

    return render_template('management/employee_info.html', users=users, userStats=userStats, title='PLACEHOLDER - Employee Information', addEmployeeForm=addEmployeeForm, removeEmployeeForm=removeEmployeeForm)



@bp.route('/add_employee', methods=['POST'])
@login_required
def add_employee():

    #Pull user data from database
    users = db.session.query(User.__table__).all()
    user = db.session.scalar(
            sa.select(User).where(User.id == session['user_id']))

    addEmployeeForm = AddEmployeeForm()

    if addEmployeeForm.validate_on_submit():
        # Check if entered user id is unique
        newID = db.session.scalar(
            sa.select(User).where(User.id == addEmployeeForm.id.data))
        if newID:
            flash("Employee ID must be unique")
        else:
            newUser = User(id = addEmployeeForm.id.data, name = addEmployeeForm.name.data, role = addEmployeeForm.role.data)

            db.session.add(newUser)
            db.session.commit()
            # Refresh page
            return redirect(url_for('management.employee_info'))

    return redirect(url_for('management.employee_info'))

@bp.route('/remove_employee', methods=['POST'])
@login_required
def remove_employee():
    #Pull user data from database
    users = db.session.query(User.__table__).all()
    user = db.session.scalar(
            sa.select(User).where(User.id == session['user_id']))

    removeEmployeeForm = RemoveEmployeeForm()

    if removeEmployeeForm.validate_on_submit():
        rmUser = db.session.scalar(sa.select(User).where(User.id == removeEmployeeForm.id.data))
        # Check if entered user id is unique
        
        if not rmUser:
            flash("Invalid ID")
        else:

            db.session.delete(rmUser)
            db.session.commit()
            # Refresh page
            return redirect(url_for('management.employee_info'))

    return redirect(url_for('management.employee_info'))