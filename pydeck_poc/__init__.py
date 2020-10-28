from flask import Flask
from os import environ
from dotenv import load_dotenv
from os.path import join, dirname
from flask_basicauth import BasicAuth


application = Flask(__name__)
basic_auth = BasicAuth(application)

# Secret key for form
application.config['SECRET_KEY'] = environ.get('SECRET_KEY')

# Basic auth
application.config['BASIC_AUTH_USERNAME'] = environ.get('BASIC_AUTH_USERNAME')
application.config['BASIC_AUTH_PASSWORD'] = environ.get('BASIC_AUTH_PASSWORD')

# Mapbox
application.config['MAPBOX_AUTH'] = environ.get('MAPBOX_AUTH')


from pydeck_poc import routes