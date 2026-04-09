from typing import Optional
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
    # NAME - Not unique !!MAY BE REPLACED BY USERNAME LATER
    name: so.Mapped[str] = so.mapped_column(sa.String(64), unique=False)
    # PASSWORD_HASH: Hashed for security
    password_hash: so.Mapped[Optional[str]] = so.mapped_column(sa.String(256))

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

    def __repr__(self):
        return '<User {}>'.format(self.name)
