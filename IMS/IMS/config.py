import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:

    # Configure database - HARDCODED, CHANGE LATER
    # NOTE: No password currently because 'md5' wouldn't work. Currently set to 'trust'
    #       in '/var/lib/pgsql/data/pg_hba.conf'. Consider changing if a workaround is found.
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')  or \
                                'sqlite:///' + os.path.join(basedir, 'IMS.db')
                                #'postgresql://localhost/flask_test?user=brandon'

    # Set the secret key
    SECRET_KEY = 'G883//~b49#a%xcaosgifoaiutiajkc059145185ugdjlfz,'
