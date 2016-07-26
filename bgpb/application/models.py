from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

from bgpb.application import app, db, lm, UserMixin


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    social_id = db.Column(db.String(64), nullable=False, unique=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    is_admin = db.Column(db.Boolean, nullable=False)

    @staticmethod
    def make_unique_name(username):
        if User.query.filter_by(username=username).first() is None:
            return username
        version = 2
        while True:
            new_username = username + str(version)
            if User.query.filter_by(username=new_username).first() is None:
                break
            version += 1
        return new_username

    @property
    def is_authenticated(self):
        return True

    @property
    def is_active(self):
        return True

    @property
    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.id)

    def __repr__(self):
        return '<User %r>' % self.username


@lm.user_loader
def load_user(userid):
    return User.query.get(int(userid))


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(140), nullable=False, unique=True)
    body = db.Column(db.Text, nullable=False)
    timestamp = db.Column(db.DateTime, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    tags = relationship('Tag', backref='post')

    def __repr__(self):
        return '<Post %r>' % self.body


class Tag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    post_id = db.Column(db.Integer, ForeignKey('post.id'))

    def __repr__(self):
        return '<Tag %r>' % self.name
