from flask import Flask
from flask_login import LoginManager, UserMixin
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, template_folder='../templates', static_folder='../static')
app.config.from_object('config')
db = SQLAlchemy(app)
lm = LoginManager(app)

lm.init_app(app)
lm.login_view = 'index'

from bgpb.templates import *
from . import views, models

