from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.fields.datetime import DateField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):

    email = StringField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Sign in')
    
class RegistrationForm(FlaskForm):
    firstName = StringField('FirstName',validators=[DataRequired()] )
    lastName = StringField('lastName',validators=[DataRequired()] )
    adress = StringField('Adress',validators=[DataRequired()] )
    dateOfBirth = DateField('dateOfBirth', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])