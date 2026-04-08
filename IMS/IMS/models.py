from typing import Optional
import sqlalchemy as sa
import sqlalchemy.orm as so
from IMS import db

"""                                                        """
#               Module - models.py                           #
#   Defines database models that are used to                 #
#   create, alter and access the application's database      #
"""                                                        """



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
class User(db.Model):
    # ID - PRIMARY KEY
    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    # NAME - Not unique !!MAY BE REPLACED BY USERNAME LATER
    name: so.Mapped[str] = so.mapped_column(sa.String(64), unique=False)
    # PASSWORD_HASH: Hashed for security
    password_hash: so.Mapped[Optional[str]] = so.mapped_column(sa.String(256))

    def __repr__(self):
        return '<User {}>'.format(self.name)
