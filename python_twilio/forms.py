from flask_wtf import FlaskForm
from flask_wtf.recaptcha import validators
from wtforms.fields.core import Label
from wtforms.fields.simple import PasswordField
from wtforms.fields.html5 import TelField
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import DataRequired, Length, data_required,length,EqualTo,Email

class RegistrationForm(FlaskForm): 
    username = StringField(label='Username',validators=[DataRequired(),Length(min=3,max=18)])
    email = StringField(label='Email',validators=[DataRequired(), Email()])
    mobilenumber = TelField(label='Mobile Number',validators=[Length(min=12)])
    password = PasswordField(label='Password',validators=[DataRequired(),Length(min=6,max=16)])
    confirm_password = PasswordField(label='Confirm Password',validators=[DataRequired(),EqualTo('password')])
    submit = SubmitField(label='Sign Up')


class LoginForm(FlaskForm): 
    email = StringField(label='Email',validators=[DataRequired(), Email()])
    password = PasswordField(label='password',validators=[DataRequired(),Length(min=6,max=16)])
    submit = SubmitField(label='Login')

