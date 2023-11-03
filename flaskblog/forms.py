from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField, SelectField, SearchField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flaskblog.models import User


class RegistrationForm(FlaskForm):
    first_name = StringField('First name', validators=[
        DataRequired(), Length(min=2, max=20)])
    last_name = StringField('Last name', validators=[
        DataRequired(), Length(min=2, max=20)])

    dynamic_selection = SelectField(u'You are joining as?', choices=[
        ('Writer', 'Writer'),
        ('Reader', 'Reader'),
    ])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[
        DataRequired(), EqualTo('password')])
    submit = SubmitField('Create account')


def validate_username(self, first_name, last_name):
    user = User.query.filter_by(first_name=first_name.data, last_name=last_name.data).first()
    if user:
        raise ValidationError(
            'Username is taken! Please choose another one')


def validate_email(self, email):
    user = User.query.filter_by(email=email.data).first()
    if user:
        raise ValidationError('Email is taken! Please choose another one')


class LoginForm(FlaskForm):
     email = StringField('Email address', validators=[DataRequired()])
     password = PasswordField(
        'Password', validators=[DataRequired()])
     submit = SubmitField('Login')




class PostForm(FlaskForm):
    search = SearchField()
    title = StringField('Title', validators=[DataRequired()])
    content = TextAreaField('Content', validators=[DataRequired()])
    submit = SubmitField('Publish')
