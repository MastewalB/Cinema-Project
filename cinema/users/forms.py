from flask_wtf import FlaskForm, RecaptchaField
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, SubmitField, PasswordField, BooleanField, RadioField, TextField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flask_login import current_user
from cinema.models import User



class RegistrationForm( FlaskForm ):
    """This is a Registration Form for a new Employee"""

    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    gender = RadioField('gender', choices=[('M', 'Male'),('F', 'Female'), ('O', 'unknown')])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    recaptcha = RecaptchaField()

    submit = SubmitField('Submit Information')

    def validate_username( self, username ):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError("The Username is already taken")
    def valiate_email(self, email):

        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('The Email is already Taken')

class LoginForm(FlaskForm):
    
    email = StringField('Email', validators=[DataRequired(),Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')

class UpdateAccountForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    picture = FileField( 'Update Profile Picture', validators=[FileAllowed(['jpg','png'])] )
    email = StringField('Email', validators=[DataRequired(), Email()])
    
    
    submit = SubmitField('Update')

    def valiate_username(self, username):
        
        if username.data != current_user.username:
            user = User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError('The Username is already Taken')

    def valiate_email(self, email):

        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError('The Email is already Taken')

