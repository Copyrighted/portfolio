from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField('이메일', validators=[DataRequired()])
    password = PasswordField('암호', validators=[DataRequired()])
    remember_me = BooleanField('날 기억해')
    submit = SubmitField('암호')