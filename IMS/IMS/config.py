import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:

    # Configure database - HARDCODED, CHANGE LATER
    # NOTE: No password currently because 'md5' wouldn't work. Currently set to 'trust'
    #       in '/var/lib/pgsql/data/pg_hba.conf'. Consider changing if a workaround is found.
    SQLALCHEMY_DATABASE_URI = 'postgresql://localhost/flask_test?user=brandon'
