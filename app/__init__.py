from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from . import config_options


db = SQLAlchemy()


#intitalize application

def create_app(config_name):

    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(config_options[config_name])
    app.config.from_object('config.py')
    db.init_app(app)
    
    return app



