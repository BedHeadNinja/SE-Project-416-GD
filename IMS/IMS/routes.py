from flask import render_template, Blueprint
from IMS import app

# Routes

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html',title='PLACEHOLDER')
