"""

            ### OBSOLETE - REMOVE ###


"""
"""

from flask import render_template, flash, redirect, url_for, session
from flask_login import current_user, login_user, logout_user, login_required
import sqlalchemy as sa

#! Local Imports!#
from IMS import app, db
from IMS.models import User, Product, Order
from IMS.forms import IDForm, PasswordForm, AddProductForm, RemoveProductForm, OrderProductForm

#!!!!! TEMP - REPLACE WITH arrivalTime() BLACKBOX FUNCTION !!!!!
from datetime import datetime, timezone
"""
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

@app.route('/')
@app.route('/index')
@login_required
def index():
    return render_template('index.html',title='PLACEHOLDER')
"""
"""
#               Function: loginID
# - Handles the first stage of the login process.
#   Gets the user's ID and verifies that it exists in
#   the database.
# - Redirects the user to registerPassword if there
#   is no password associated with the given valid ID.
#

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
            sa.select(User).where(User.id == user_input['id']))
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

"""
#   Function: inventory
#   Handles displaying and managing inventory
#   !!INCOMPLETE!!
"""
"""
@app.route('/inventory', methods=['GET','POST'])
@login_required
def inventory():
    #Pull product data from database
    products = db.session.query(Product.__table__).all()

    # Create form objects
    addProductForm = AddProductForm()
    removeProductForm = RemoveProductForm()
    orderProductForm = OrderProductForm()

    return render_template('inventory/inventory.html',title='PLACEHOLDER', products=products, addProductForm=addProductForm, removeProductForm=removeProductForm, orderProductForm=orderProductForm)

@app.route('/inventory/add_product', methods=['GET','POST'])
@login_required
def add_product():

    # Create form objects
    addProductForm = AddProductForm()
    removeProductForm = RemoveProductForm()
    orderProductForm = OrderProductForm()

    # If the user chooses to add a product, add its values to the database
    if addProductForm.validate_on_submit():
        newProduct = Product(product_name=addProductForm.product_name.data, on_hand_count=addProductForm.on_hand_count.data)
        db.session.add(newProduct)
        db.session.commit()
        # Refresh page
        return redirect(url_for('inventory'))

    return render_template('inventory/inventory.html',title='PLACEHOLDER', products=products, addProductForm=addProductForm, removeProductForm=removeProductForm, orderProductForm=orderProductForm)


@app.route('/inventory/remove_product', methods=['GET','POST'])
@login_required
def remove_product():

    # Create form objects
    addProductForm = AddProductForm()
    removeProductForm = RemoveProductForm()
    orderProductForm = OrderProductForm()

    # If the user chooses to remove a product, delete it from the database
    if removeProductForm.validate_on_submit():
        #print("Here's the problem")
        removingProduct = db.session.scalar(sa.select(Product).where(Product.product_id == removeProductForm.product_id.data))
        # If no matching product id is found, return an error message
        if not removingProduct:
            flash("Invalid ID")
        else:
            db.session.delete(removingProduct)
            db.session.commit()
            # Refresh page
            return redirect(url_for('inventory'))


    return render_template('inventory/inventory.html',title='PLACEHOLDER', products=products, addProductForm=addProductForm, removeProductForm=removeProductForm, orderProductForm=orderProductForm)

@app.route('/inventory/order_product', methods=['GET','POST'])
@login_required
def order_product():

    # Create form objects
    addProductForm = AddProductForm()
    removeProductForm = RemoveProductForm()
    orderProductForm = OrderProductForm()

    #If the user chooses to order an item, place an order and add the data to the database
    if orderProductForm.validate_on_submit():
        orderedProduct = db.session.scalar(sa.select(Product).where(Product.product_id == orderProductForm.product_id.data))
        #orderedProduct = None
        if not orderedProduct:
            flash("Invalid ID")
        else:
            #Create and add an order
            order = Order(
                        product_id=orderProductForm.product_id.data,
                        quantity=orderProductForm.quantity.data,
                        arrival_time=datetime.now(timezone.utc))
            db.session.add(order)
            # Update the on-order count of the product that's been ordered
            orderedProduct.on_order_count=orderProductForm.quantity.data
            db.session.commit()
            # Refresh Page
            return redirect(url_for('inventory'))


    return render_template('inventory/inventory.html',title='PLACEHOLDER', products=products, addProductForm=addProductForm, removeProductForm=removeProductForm, orderProductForm=orderProductForm)

@app.route('/management/employee_info')
@login_required
def employee_info():

   return render_template('management/employee_info.html', title='PLACEHOLDER - Employee Information')
"""



