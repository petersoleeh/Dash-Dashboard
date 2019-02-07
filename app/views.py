from flask import render_template, redirect
from app import flask_app
import flask
import dashapp





#index page
@flask_app.route('/')
def index():
    '''
    index page with the landing page and data
    '''
    title = 'Dash Template Test'
    
    return render_template('index.html',title=title)



