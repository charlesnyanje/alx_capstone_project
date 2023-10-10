from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, validators, SelectField, PasswordField, TextAreaField
from wtforms.validators import DataRequired, EqualTo, Length,  ValidationError


class RegistrationForm(FlaskForm):
    first_name = StringField('First name', validators=[
                             DataRequired(), Length(min=4, max=25)])
    last_name = StringField('Last name', validators=[
                            DataRequired(), Length(min=4, max=25)])
    dynamic_selection = SelectField(u'You are joining as?', choices=[
        ('Writer', 'Writer'),
        ('Reader', 'Reader'),
    ])
    email = StringField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[
                                   DataRequired(), EqualTo('password')])
    submit = SubmitField('Create account')


class LoginForm(FlaskForm):
    email = email = StringField('Email address', validators=[DataRequired()])
    password = password = PasswordField(
        'Password', validators=[DataRequired()])
    submit = SubmitField('Login')
