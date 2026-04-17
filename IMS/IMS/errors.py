from flask import render_template
from IMS import app, db

"""                                   """
#           Module: Errors.py           #
#   Provides custom error handlers      #
#           for the program             #
"""                                   """


# Handles 404 errors with a custom page
@app.errorhandler(404)
def not_found_error(error):
    return render_template('errors/404.html'), 404


# Handles 500 errors with a custom page
@app.errorhandler(500)
def internal_error(error):
    # Roll back the database session
    db.session.rollback()
    return render_template('errors/500.html'), 500
