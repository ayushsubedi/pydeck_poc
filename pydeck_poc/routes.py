
from flask import render_template
from pydeck_poc import application
from pydeck_poc import basic_auth
from pydeck_poc.helper import deck_example

@application.route('/')
def index():
    return deck_example()
