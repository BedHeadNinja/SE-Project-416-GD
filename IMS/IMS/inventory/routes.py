from flask import current_app, render_template, flash, redirect, url_for, session
from flask_login import current_user, login_user, logout_user, login_required
import sqlalchemy as sa

#! Local Imports!#
from IMS import db
from IMS.models import Product, Order, User
from IMS.inventory import bp
from IMS.inventory.forms import AddProductForm, RemoveProductForm, OrderProductForm, AddEmployeeForm

#!!!!! TEMP - REPLACE WITH arrivalTime() BLACKBOX FUNCTION !!!!!
from datetime import datetime, timezone

"""
#   Function: inventory
#   Handles displaying and managing inventory
#   !!INCOMPLETE!!
"""
@bp.route('/inventory', methods=['GET','POST'])
@login_required
def inventory():
    #Pull product data from database
    products = db.session.query(Product.__table__).all()

    # Create form objects
    addProductForm = AddProductForm()
    removeProductForm = RemoveProductForm()
    orderProductForm = OrderProductForm()

    return render_template('/inventory/inventory.html',title='PLACEHOLDER', products=products, addProductForm=addProductForm, removeProductForm=removeProductForm, orderProductForm=orderProductForm)

@bp.route('/add_product', methods=['GET','POST'])
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
        return redirect(url_for('inventory.inventory'))

    return render_template('/inventory/inventory.html',title='PLACEHOLDER', products=products, addProductForm=addProductForm, removeProductForm=removeProductForm, orderProductForm=orderProductForm)


@bp.route('/remove_product', methods=['GET','POST'])
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
            return redirect(url_for('inventory.inventory'))


    return render_template('/inventory/inventory.html',title='PLACEHOLDER', products=products, addProductForm=addProductForm, removeProductForm=removeProductForm, orderProductForm=orderProductForm)

@bp.route('/order_product', methods=['GET','POST'])
@login_required
def order_product():

    # Create form objects
    addProductForm = AddProductForm()
    removeProductForm = RemoveProductForm()
    orderProductForm = OrderProductForm()

    #If the user chooses to order an item, place an order and add the data to the database
    if orderProductForm.validate_on_submit():
        orderedProduct = db.session.scalar(sa.select(Product).where(Product.product_id == orderProductForm.product_id.data))
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
            return redirect(url_for('inventory.inventory'))


    return render_template('/inventory/inventory.html',title='PLACEHOLDER', products=products, addProductForm=addProductForm, removeProductForm=removeProductForm, orderProductForm=orderProductForm)

@bp.route('/management/employee_info')
@login_required
def employee_info():

    #Pull user data from database
    users = db.session.query(User.__table__).all()
    user = db.session.scalar(
            sa.select(User).where(User.id == session['user_id']))

    if user.role != 'Manager':
        flash("You do not have access to this page!")
        return redirect('/index')

    addEmployeeForm = AddEmployeeForm()

    return render_template('management/employee_info.html', users = users, title='PLACEHOLDER - Employee Information', addEmployeeForm = addEmployeeForm)

@bp.route('/management/add_employee', methods=['POST'])
def add_employee():

    addEmployeeForm = AddEmployeeForm()

    if addEmployeeForm.validate_on_submit():
        newUser = User(id = addEmployeeForm.id.data, name = addEmployeeForm.name.data, role = addEmployeeForm.role.data)

        db.session.add(newUser)
        db.session.commit()
        # Refresh page
        return redirect(url_for('inventory.employee_info'))
    
    return render_template('management/employee_info.html', users = users, title='PLACEHOLDER - Employee Information', addEmployeeForm = addEmployeeForm)
