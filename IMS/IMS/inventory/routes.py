from flask import current_app, render_template, flash, redirect, url_for, session, request
from flask_login import current_user, login_user, logout_user, login_required
import sqlalchemy as sa

#! Local Imports!#
from IMS import db
from IMS.models import Product, Order, User
from IMS.inventory import bp
from IMS.inventory.forms import AddProductForm, RemoveProductForm, UpdateQuantityForm

#!!!!! TEMP - REPLACE WITH arrivalTime() BLACKBOX FUNCTION !!!!!
from datetime import datetime, timezone

"""
#   Function: inventory
#   Handles displaying and managing inventory
#   !!INCOMPLETE!!
"""
@bp.route('/', methods=['GET','POST'])
@login_required
def inventory():
    # Pull product data from database
    products = db.session.query(Product.__table__).all()

    # List of product states
    productStats = [len(products), 0, 0]

    # Create form objects
    addProductForm = AddProductForm()
    removeProductForm = RemoveProductForm()
    updateQuantityForm = UpdateQuantityForm()

    # Gather product states from product data
    for product in products:
        # If the total count is at or below the minimum, add to low stock count
        if (product.on_hand_count + product.on_order_count <= product.stock_alert_minimum):
            productStats[1] += 1
        # If the total count is within 50 of the minimum, add to expiring count
        elif (product.on_hand_count + product.on_order_count <= product.stock_alert_minimum + 50):
            productStats[2] += 1

    return render_template('/inventory/inventory.html',title='PLACEHOLDER', products=products, productStats=productStats, addProductForm=addProductForm, removeProductForm=removeProductForm, updateQuantityForm=updateQuantityForm)


@bp.route('/add_product', methods=['GET','POST'])
@login_required
def add_product():

    # Create form objects
    addProductForm = AddProductForm()

    # If the user chooses to add a product, add its values to the database
    if addProductForm.validate_on_submit():
        newProduct = Product(product_name=addProductForm.product_name.data ,on_hand_count = addProductForm.on_hand_count.data)
        # If no product was found, throw an error message
        if not newProduct:
            flash("ERROR: Invalid ID")
        else:
            db.session.add(newProduct)
            db.session.commit()
            # Refresh page
            return redirect(url_for('inventory.inventory'))

    return redirect(url_for('inventory.inventory'))


@bp.route('/remove_product', methods=['GET','POST'])
@login_required
def remove_product():

    # Create form object
    removeProductForm = RemoveProductForm()

    # If the user chooses to remove a product, delete it from the database
    if removeProductForm.validate_on_submit():
        removingProduct = db.session.scalar(sa.select(Product).where(Product.product_id == removeProductForm.product_id.data))
        # If no matching product id is found, return an error message
        if not removingProduct:
            flash("Invalid ID")
        else:
            db.session.delete(removingProduct)
            db.session.commit()
            # Refresh page
            return redirect(url_for('inventory.inventory'))

    return redirect(url_for('inventory.inventory'))

@bp.route('/order_product', methods=['GET','POST'])
@login_required
def order_product():

    # If the user chooses to order products, update the on order count
    if request.method == 'POST':
        # Get order data
        orderedProducts = request.form

        # Separate order data into lists
        product_id_list = orderedProducts.getlist('product_id')
        quantity_list = orderedProducts.getlist('quantity')

        # Loop through product ids to update on order counts
        for i in range(len(product_id_list)):
            product = db.session.scalar(sa.select(Product).where(Product.product_id == product_id_list[i]))
            # If no product matching the id was found, return an error
            if not product:
                    flash("ERROR: Invalid Product ID Received")
            else:
                product.on_order_count += int(quantity_list[i])
                db.session.commit()
                # Refresh page
                return redirect(url_for('inventory.inventory'))

    return redirect(url_for('inventory.inventory'))

@bp.route('/update_quantity', methods=['GET','POST'])
@login_required
def update_quantity():
    # Pull product data from database
    #products = db.session.query(Product.__table__).all()

    # List of product states
    #productStats = [len(products), 0, 0]

    # Create form object
    updateQuantityForm = UpdateQuantityForm()

    #If the user chooses to order an item, place an order and add the data to the database
    if updateQuantityForm.validate_on_submit():
        updatedProduct = db.session.scalar(sa.select(Product).where(Product.product_id == updateQuantityForm.product_id.data))
        if not updatedProduct:
            flash("Invalid ID")
        else:
            # Update the on-order count of the product that's been ordered
            updatedProduct.on_hand_count=updateQuantityForm.quantity.data
            db.session.commit()
            # Refresh Page
            return redirect(url_for('inventory.inventory'))

    return redirect(url_for('inventory.inventory'))
