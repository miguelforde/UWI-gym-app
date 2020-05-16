from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, TextAreaField, SubmitField

from wtforms.validators import InputRequired, EqualTo, Email

class SignUp(FlaskForm):
  fname = StringField('First Name', validators=[InputRequired()])
  lname = StringField('Last Name', validators=[InputRequired()])
  username = StringField('Username', validators=[InputRequired()])
  dob = StringField('Date of Birth', validators=[InputRequired()])
  email = StringField('Email', validators=[Email(), InputRequired()])
  password = PasswordField('New Password', validators=[InputRequired(), EqualTo('confirm', message='Passwords must match')])
  confirm  = PasswordField('Repeat Password')
  submit = SubmitField('SIGN UP')


class LogIn(FlaskForm):
  username = StringField('Username', validators=[InputRequired()])
  password = PasswordField('Password', validators=[InputRequired()])
  submit = SubmitField('LOGIN')
