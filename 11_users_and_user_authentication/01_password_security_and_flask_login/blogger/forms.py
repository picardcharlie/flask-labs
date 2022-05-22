from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, PasswordField, BooleanField
from wtforms.fields import EmailField
from wtforms.validators import DataRequired, Length, Email, ValidationError
from .models import db, User

def length_check(form,field):
    if len(field.data) == 0:
        raise ValidationError('Fields should not be null')


class AddPostForm(FlaskForm):
    title = StringField('Title', validators=[ DataRequired()])
    description = TextAreaField('Description', validators = [DataRequired()])


class SignUpForm(FlaskForm):
    firstname = StringField('First Name', validators= [DataRequired(), Length(min=1)])
    lastname = StringField('Last Name', validators= [DataRequired()])
    username = StringField('User Name', validators= [ DataRequired(), Length(min=4)])
    password = PasswordField('Password',validators=[ DataRequired(), Length(min=6)])
    email = EmailField('Email', validators= [DataRequired(), Email()])
    submit = SubmitField('Sign Up')

    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError("Username unavailable")

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError("Email unavailable")


class SignInForm(FlaskForm):
    email = EmailField('Email', validators = [DataRequired(), Email()])
    password = PasswordField('Password', validators = [DataRequired(), Length(min=6, max=30)])
    remember_me = BooleanField('Keep me logged in')
    submit = SubmitField('Sign In')

class AboutUserForm(FlaskForm):
    firstname= StringField('First Name', validators= [DataRequired(), length_check])
    lastname = StringField('Last Name', validators= [DataRequired()])
    username = StringField('User Name', validators= [ DataRequired(), Length(min=4)])
    password = PasswordField('Password',validators=[ DataRequired(), Length(min=6)])
    email = EmailField('Email', validators= [DataRequired(), Email()])
