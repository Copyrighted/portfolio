from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField('Login', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember me')
    submit = SubmitField('Submit')

class PostForm(FlaskForm):
    title = StringField(validators=[DataRequired()])
    post = TextAreaField(validators=[DataRequired()])
    submit = SubmitField('Submit')

class DeleteForm(FlaskForm):
    delete = SubmitField('Submit')

class EditPostForm(FlaskForm):
    title = StringField(validators=[DataRequired()])
    post = TextAreaField(validators=[DataRequired()])
    update = SubmitField('Submit')
