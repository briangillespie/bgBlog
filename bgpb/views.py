from flask import render_template, url_for

from bgpb import app

@app.route('/')
@app.route('/index')
def index():
    greeting = "Welcome to the Brian Gillespie blog!"
    posts = []
    title = 'Home Page'
    return render_template('index.html', **locals())