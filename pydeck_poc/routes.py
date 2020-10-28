
from flask import render_template
from pydeck_poc import application
from pydeck_poc import basic_auth
from pydeck_poc.helper import deck_example1, deck_example2
import random


@application.route('/')
def index():
    random_plot = [deck_example1(), deck_example2()]
    return render_template('poc.html',
                            first = random.choice(random_plot))

