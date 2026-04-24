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

    # Create form objects
    addProductForm = AddProductForm()
    removeProductForm = RemoveProductForm()
    updateQuantityForm = UpdateQuantityForm()

    return render_template('/inventory/inventory.html',title='PLACEHOLDER', products=products, addProductForm=addProductForm, removeProductForm=removeProductForm, updateQuantityForm=updateQuantityForm)


@bp.route('/add_product', methods=['GET','POST'])
@login_required
def add_product():
    # Pull product data from database
    products = db.session.query(Product.__table__).all()

    # Create form objects
    addProductForm = AddProductForm()
    removeProductForm = RemoveProductForm()
    updateQuantityForm = UpdateQuantityForm()

    # If the user chooses to add a product, add its values to the database
    if addProductForm.validate_on_submit():
        newProduct = Product(product_name=addProductForm.product_name.data, on_hand_count=addProductForm.on_hand_count.data)
        if not newProduct:
            flash("ERROR: Invalid ID")
        else:
            db.session.add(newProduct)
            db.session.commit()
            # Refresh page
            return redirect(url_for('inventory.inventory'))

    return render_template('/inventory/inventory.html',title='PLACEHOLDER', products=products, addProductForm=addProductForm, removeProductForm=removeProductForm, updateQuantityForm=updateQuantityForm)


@bp.route('/remove_product', methods=['GET','POST'])
@login_required
def remove_product():
    # Pull product data from database
    products = db.session.query(Product.__table__).all()

    # Create form objects
    addProductForm = AddProductForm()
    removeProductForm = RemoveProductForm()
    updateQuantityForm = UpdateQuantityForm()

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


    return render_template('/inventory/inventory.html',title='PLACEHOLDER', products=products, addProductForm=addProductForm, removeProductForm=removeProductForm, updateQuantityForm=updateQuantityForm)

@bp.route('/order_product', methods=['GET','POST'])
@login_required
def order_product():
    #Pull product data from database
    products = db.session.query(Product.__table__).all()

    # Create form objects
    addProductForm = AddProductForm()
    removeProductForm = RemoveProductForm()
    updateQuantityForm = UpdateQuantityForm()

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
                #print(f"product_id: {product_id_list[i]}\nquantity: quantity_list[i]")

    return render_template('/inventory/inventory.html',title='PLACEHOLDER', products=products, addProductForm=addProductForm, removeProductForm=removeProductForm, updateQuantityForm=updateQuantityForm)


@bp.route('/update_quantity', methods=['GET','POST'])
@login_required
def update_quantity():
    # Pull product data from database
    products = db.session.query(Product.__table__).all()

    # Create form objects
    addProductForm = AddProductForm()
    removeProductForm = RemoveProductForm()
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

    return render_template('/inventory/inventory.html',title='PLACEHOLDER', products=products, addProductForm=addProductForm, removeProductForm=removeProductForm, updateQuantityForm=updateQuantityForm)

