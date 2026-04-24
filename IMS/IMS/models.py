from typing import Optional
from datetime import datetime, timezone
from uuid import UUID, uuid4
import sqlalchemy as sa
import sqlalchemy.orm as so
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

#! Local Imports!#
from IMS import db, login

"""                                                        """
#               Module - models.py                           #
#   Defines database models that are used to                 #
#   create, alter and access the application's database      #
#                                                            #
"""                                                        """

"""
#       Function - user_loader
#   Used by Flask-Login to load a User, allowing the module
#   to keep track of that logged-in user.
#   Enables 'remember me' functionality for site.
#
"""
@login.user_loader
def load_user(id):
    # Access the database and get the current user's id
    # NOTE: id parameter is recieved as a string, so it needs to be
    #       typecase to int when querying the database.
    return db.session.get(User, int(id))

"""
#       Class - User
#   Represents a user in the system
#
#   Data:
#       id: Employee ID. Primary Key
#       name: Employee name
#       password-hash: Account password. Hashed for security
#
"""
class User(UserMixin, db.Model):
    # ID - PRIMARY KEY
    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    # USERNAME
    #username: so.mapped[str] = so.mapped_column(sa.String(64), index=True, unique=True)
    # !!!TESTING!!! EMAIL
    #email: so.mapped[str] = so.mapped_column(sa.String(120), index=True, unique=True)
    # NAME - Not unique !!MAY BE REPLACED BY USERNAME LATER
    name: so.Mapped[str] = so.mapped_column(sa.String(64), unique=False)
    # PASSWORD_HASH: Hashed for security
    password_hash: so.Mapped[Optional[str]] = so.mapped_column(sa.String(256))
    # ROLE: User's role. Employee by default
    role: so.Mapped[str] = so.mapped_column(sa.String(20), default='employee', nullable=False)

    """
    #               Function - set_password
    #   Hashes a user's password before storing it to the database
    #
    """
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    """
    #       Function - check_password
    #   Uses werkzeug's check_password_hash method to verify
    #   that a user's password matches the hash
    #
    """
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    # def __init__(self, **kwargs):
    # if 'id' not in kwargs:
    #   kwargs['id'] == uuid4()
    #super

    # Returns a list of column descriptions
    def __repr__(self):
        return '<User(id={},name={})>'.format(self.id, self.name)

"""
#       Table: Product
#   Represents a product in the system
#
#   Data:
#       id: Product ID. Primary key
#       name: Name of the product
#       !! CONSIDER RENAMING THE FOLLOWING:
#       on_hand_count: Quantity of the product on hand
#       on_order_count: Quantity of the product currently ordered
#
"""
class Product(db.Model):
    # PRODUCT ID - PRIMARY KEY #!!!TESTING!!!
    product_id: so.Mapped[int] = so.mapped_column(primary_key=True, unique=True, autoincrement=True)
    # PRODUCT NAME
    product_name: so.Mapped[str] = so.mapped_column(sa.String(64), unique=False)
    # CURRENT PRODUCT COUNT
    on_hand_count: so.Mapped[int] = so.mapped_column()
    # PRODUCT ON ORDER
    on_order_count: so.Mapped[int] = so.mapped_column(default=0)
    # STOCK ALERT MINIMUM - The lowest stock quantity reached before an alert is raised. Null by default
    stock_alert_minimum: so.Mapped[int] = so.mapped_column(nullable=True)

    # Sets default values on object creation
    # NOTE: This is required to prevent errors. Both product id and on_order_count will, with
    #       the current configuration, never be sent a value as an argument, and would therefore otherwise be null - very bad!
    def __init_(self, **kwargs):
        # !!OUTDATED!! If no product id is sent, generate one (will always execute)
        #if 'product_id' not in kwargs:
        #    kwargs['product_id'] = uuid4()
        # If no on order count is sent, set to 0 (will always execute)
        if 'on_order_count' not in kwargs:
            kwargs['on_order_count'] = 0
        super().__init__(**kwargs)

    # Returns a list of column descriptions
    def __repr__(self):
        return '<Product(id={}, name={}, on_hand_count={}, on_order_count={})>'.format(self.product_id,self.product_name,self.on_hand_count,self.on_order_count)


#!!!IN PROGRESS!!!#
"""
#       Table: Order
#   Represents an order in the system
#
#   Data:
#       order_id: Order ID. Primary key
#       product_id: Product ID. Identifies which item is ordered
#       quantity: Quantity of the product ordered
#       timestamp: Date and time the order was placed
#       arrival_time: Current estimated arrival time
#
"""
class Order(db.Model):
    # ORDER ID - PRIMARY KEY
    order_id: so.Mapped[UUID] = so.mapped_column(primary_key=True, unique=True, default=uuid4)
    # PRODUCT ID
    product_id: so.Mapped[int] = so.mapped_column()
    # QUANTITY
    quantity: so.Mapped[int] = so.mapped_column(default=0)
    # TIMESTAMP
    timestamp: so.Mapped[datetime] = so.mapped_column(
            index=True, default=lambda: datetime.now(timezone.utc))
    # ARRIVAL TIME
    arrival_time: so.Mapped[datetime] = so.mapped_column(
            index=True)

    # Sets default values on object creation
    def __init__(self, **kwargs):
        if 'order_id' not in kwargs:
            kwargs['order_id'] = uuid4()
        super().__init__(**kwargs)

    # Returns a list of column descriptions
    def __repr__(self):
        return '<Order(order_id={}, product_id={}, quantity={}, timestamp={}, arrival_time={})>'.format(
                self.order_id,self.product_id,self.quantity, self.timestamp, self.arrival_time)
"""
class LineItem(db.model):
    # ORDER ID - PRIMARY KEY
    # NOTE: Ties line item to its order
    order_id: so.Mapped[UUID] = so.mapped_column(primary_key=True, unique=True, default-uuid4)
    # PRODUCT ID
    product_id: so.Mapped[int] =so.mapped_column()
    # QUANTITY
    quantity: so.Mapped[int] = soo.mapped_column(default=0)
"""


