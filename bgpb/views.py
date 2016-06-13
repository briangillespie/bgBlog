from flask import render_template, url_for

from bgpb import app

@app.route('/')
@app.route('/index')
def index():
    user = {'name': 'Visitor'}
    posts = []
    title = 'Home Page'
    return render_template('index.html', **locals())