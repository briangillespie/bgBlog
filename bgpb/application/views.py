import markdown
from flask import render_template, url_for, redirect, flash, Markup, g
from flask_login import current_user, login_user, logout_user, session
from oauth import *
from bgpb.application import app, db, lm
from .models import User, Post, Tag
from .forms import PostForm
from datetime import datetime


@app.route('/')
@app.route('/index')
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


@app.route('/resume')
def resume():
    return render_template('resume.html', **locals())


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.before_request
def before_request():
    g.user = current_user
    if g.user.is_authenticated:
        g.user.last_seen = datetime.utcnow()
        db.session.add(g.user)
        db.session.commit()


@app.route('/post/<postname>', methods=['GET'])
def get_post(postname):
    post = Post.query.filter_by(name=postname).first()
    if not post:
        flash('Post not found')
        return redirect(url_for('index'))
        # Will need to redirect to an error message here (404)
    md_content = content = Markup(markdown.markdown(post.body))
    title = post.name
    tags = post.tags
    timestamp = post.timestamp
    return render_template('post.html', **locals())


@app.route('/post', methods=['GET', 'POST'])
def posts():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(title=form.title.data, body=form.post.data, timestamp=datetime.utcnow(), author=g.user)
        db.session.add(post)
        db.session.commit()
        flash('Your post is now live!')
        return redirect(url_for('index'))
    postsamples = [
        {
            'author': {'nickname': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'nickname': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('post.html', **locals())
    # if not request:
    #     posts = Post.query.select()
    #     if not posts:
    #         return redirect(url_for('index'))
    #         # Will need to redirect to an error message here (404)
    #     return render_template('postlist.html', **locals())
    # else:
    #     title, body, timestamp, user_id, tags = request.get_data()
    #     post = Post(title=title, body=body, timestamp=timestamp, user_id=user_id, tags=tags)
    #     db.session.add(post)
    #     db.session.commit()
    #     return redirect(url_for('get_post', postname=title))


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
        user = User(social_id=social_id, username=username, email=email, is_admin=False)
        db.session.add(user)
        db.session.commit()
    login_user(user, True)
    return redirect(url_for('index'))

