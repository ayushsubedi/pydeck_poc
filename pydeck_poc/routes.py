
from flask import render_template
from pydeck_poc import application
from pydeck_poc import basic_auth
from pydeck_poc.helper import tweet_text, deck_example



@application.route('/')
def index():
    return 'pydeck_poc'


@application.route('/basicauth')
@basic_auth.required
def basicauthtest():
    return 'it works'


@application.route('/apitest')
def apitest():
    return tweet_text()

@application.route('/deckexample')
def deckexample():
    return deck_example()