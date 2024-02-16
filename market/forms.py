from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, ValidationError
from wtforms.validators import Length, EqualTo, DataRequired, Email
from market.models import User

class RegisterForm(FlaskForm):

    def validate_username(self, username_to_check):
        user = User.query.filter_by(username=username_to_check.data).first()

        if user:
            raise ValidationError('Username already exists Please try a Different Username')
        
    def validate_email_address(self,email_address_to_check):
        email_address = User.query.filter_by(email_address=email_address_to_check.data).first() 

        if email_address:
            raise ValidationError('Email Address already exists Please try a Different Email Address')   

    username = StringField(label='User Name :', validators=[Length(min=2,max=30),DataRequired()])
    email_address = StringField(label='Email Address :',validators=[Email(), DataRequired()])
    password1 = PasswordField(label='Password :', validators=[Length(min=6), DataRequired()])
    password2 = PasswordField(label='Confirm Password :', validators=[EqualTo('password1'), DataRequired()])
    submit = SubmitField(label='Create Your Account')



class LoginForm(FlaskForm):
    username = StringField(label='User Name :',validators=[DataRequired()])
    password = PasswordField(label='Password :',validators=[DataRequired()])
    submit = SubmitField(label='Sign in')

class PurchaseItemForm(FlaskForm):
    submit = SubmitField(label='Purchase Item')

class SellItemForm(FlaskForm):
    submit = SubmitField(label='Sell Item')        