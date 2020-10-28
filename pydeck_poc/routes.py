
from flask import render_template
from pydeck_poc import application
from pydeck_poc import basic_auth
from pydeck_poc.helper import tweet_text



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

