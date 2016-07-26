from flask_wtf import Form
from wtforms import StringField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Length


class PostForm(Form):
    title = StringField('title', validators=[DataRequired()])
    post = StringField('post', validators=[DataRequired()])
