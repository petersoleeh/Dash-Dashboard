from flask import render_template
from app import app

#index page
@app.route('/')
def index():
    '''
    index page with the landing page and data
    '''
    title = 'Dash Template Test'
    
    return render_template('index.html',title=title)