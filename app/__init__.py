from flask import Flask
from flask_bootstrap import Bootstrap



# from .config import DevcConfig


# db = SQLAlchemy()


#intitalize application

flask_app = Flask(__name__)
bootstrap = Bootstrap(flask_app)

 


    
# app_dash = Dash(__name__)

# app.config.from_object(DevConfig)

# app.config.from_pyfile('config.py')
  


from app import views




