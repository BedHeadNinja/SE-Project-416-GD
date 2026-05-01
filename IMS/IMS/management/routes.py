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

    # Create form objects
    addEmployeeForm = AddEmployeeForm()
    removeEmployeeForm = RemoveEmployeeForm()

    # Check if the user is authorized to view this page
    if user.role != 'Manager'and user.role != 'manager':
        flash("You do not have access to this page!")
        return redirect('/index')

    # Get the total number of emplyees and managers
    managers_count = sum(1 for u in users if u.role and u.role.lower() == 'manager')
    employees_count = sum(1 for u in users if u.role and u.role.lower() == 'employee')
    userStats = [len(users), managers_count, employees_count]

    return render_template('management/employee_info.html', users=users, userStats=userStats, title='Employee Information', addEmployeeForm=addEmployeeForm, removeEmployeeForm=removeEmployeeForm)



@bp.route('/add_employee', methods=['POST'])
@login_required
def add_employee():

    # Create form object
    addEmployeeForm = AddEmployeeForm()

    # If the user chose to add an employee, add the employee to the database
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

    # Create form object
    removeEmployeeForm = RemoveEmployeeForm()

    # If the user chose to remove an employee, remove the employee from the database
    if removeEmployeeForm.validate_on_submit():
        rmUser = db.session.scalar(sa.select(User).where(User.id == removeEmployeeForm.id.data))

        # Check that the ID is for a valid user other than the current user
        if not rmUser:
            flash("Invalid ID")
        elif rmUser == current_user:
            flash("You cannot remove remove your own account")
        else:
            db.session.delete(rmUser)
            db.session.commit()
            # Refresh page
            return redirect(url_for('management.employee_info'))

    return redirect(url_for('management.employee_info'))

@bp.route('/manager_list_page', methods=['GET'])
@login_required
def manager_list_page():

    # Get all employees with the manager role, and display them in ascending id order
    managers = db.session.scalars(
        sa.select(User).where(
            sa.func.lower(User.role) == 'manager'
            ).order_by(User.id.asc())
        ).all()

    return render_template('/management/manager_list.html', title="Manager List", managers=managers)

@bp.route('/employee_list_page', methods=['GET'])
@login_required
def employee_list_page():

    # Get all employees with the employee role, and display them in ascending id order
    employees = db.session.scalars(
        sa.select(User).where(
            sa.func.lower(User.role) == 'employee'
            ).order_by(User.id.asc())
        ).all()
    print(employees)

    return render_template('/management/employee_list.html', title="Employee List", employees=employees)

