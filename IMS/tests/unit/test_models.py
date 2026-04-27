from IMS.models import User, Product, Order
from datetime import date, timedelta
import sqlalchemy as sa

"""
#               CLASS: test_models.py
#   Tests that each database model is correctly defined
#
"""
def test_new_user():
    """
    GIVEN a User model
    WHEN a user is created
    THEN check that the id, name, password, and role fields are correctly defined
    """

    # Create user and set attributes
    user = User(id='5000',name='test', role='employee')
    user.set_password("test")

    # Check that user data is correctly defined
    assert user.id == '5000'
    assert user.name == 'test'
    assert user.check_password('test') == True
    assert user.role == 'employee'

def test_new_product():
    """
    GIVEN a Product model
    WHEN a product is created
    THEN check that the product_id, product_name, on_hand_quantity,
         on_order_quantity, and stock_alert_minimum fields are correctly defined
    """

    # Create product and set attributes
    product = Product(product_name="Test Product", on_hand_count="500")
    #maxID = sa.scalar

    print(f"Product id: {product.product_id}")
    # Check that the product data is correctly defined
    #assert product.product_id == func.max
    assert product.product_name == "Test Product"
    assert product.on_hand_count == "500"
    assert product.on_order_count == 0
    assert product.stock_alert_minimum == 0

def test_new_order():
    """
    GIVEN an Order model
    WHEN an order is created
    THEN check that the product_id, quantity, timestamp, and arrival_time fields are correctly defined
    """

    # Create a product for the order and set attributes
    product = Product(product_name="Test Product", on_hand_count="500")

    # Set arrival time for consistant test
    arrivalTime = date.today() + timedelta(days=7)

    # Create an order and set attributes
    order = Order(quantity="500", arrival_time=arrivalTime)

    # Check that the order data is correctly defined
    #assert order.product_id == product.product_id
    assert order.quantity == '500'
    assert order.arrival_time == arrivalTime
    assert order.active == True
