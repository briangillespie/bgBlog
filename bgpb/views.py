from flask import render_template, url_for, redirect, flash
from flask_login import current_user, login_user, logout_user, session
from oauth import *
from bgpb import app, db
from models import User

@app.route('/')
# @app.route('/index')
def index():
    greeting = "Welcome to the Brian Gillespie blog!"
    posts = []
    title = 'Home Page'
    return render_template('index.html', **locals())

@app.route('/dog')
def dog():
    title = 'Dog'
    return render_template('dog.html', **locals())

@app.route('/contact')
def contact():
    title = 'Contact'
    return render_template('contact.html', **locals())

@app.route('/login')
def login():
    return render_template('login.html', **locals())

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/authorize/<provider>')
def oauth_authorize(provider):
    if not current_user.is_anonymous:
        return redirect(url_for('index'))
    oauth = OAuthSignIn.get_provider(provider)
    return oauth.authorize()


@app.route('/callback/<provider>')
def oauth_callback(provider):
    if not current_user.is_anonymous:
        return redirect(url_for('index'))
    oauth = OAuthSignIn.get_provider(provider)
    social_id, username, email = oauth.callback()
    if social_id is None:
        flash('Authentication failed.')
        return redirect(url_for('index'))
    user = User.query.filter_by(social_id=social_id).first()
    if not user:
        user = User(social_id=social_id, username=username, email=email)
        db.session.add(user)
        db.session.commit()
    login_user(user, True)
    return redirect(url_for('index'))

