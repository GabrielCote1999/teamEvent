
#from flask import Flask

#from werkzeug.utils import redirect 
#from main import app
from flask import render_template, flash, redirect, Blueprint, request
from website.models.forms import LoginForm, RegistrationForm
from .model import User, Event
from . import db


views = Blueprint('views', __name__)


@views.route("/")
# define the view using a function, which returns a string
def hello_world(name =None):
    return render_template('index.html', name = name)


@views.route('/reg', methods = ['GET', 'POST'])
def register():
    form = RegistrationForm()

    firstName = request.form.get('firstName')
    lastName = request.form.get('lastName')
    adress = request.form.get('adress')
    dateOfBirth = request.form.get('dateOfBirth')
    email = request.form.get('email')
    password = request.form.get('password')

    if form.validate_on_submit():
        flash('User {} is registred'.format(
            form.firstName, form.lastName
        ))
        newUser = User(firstName = firstName,lastName = lastName,email = email)
        db.session.add(newUser)
        db.session.commit()
        print(form.firstName, form.lastName)
        return redirect('/')
    return render_template('registration.html', title = 'Register', form = form)

@views.route('/login', methods=['GET', 'POST'])
def login():
    #passing the login form model
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}'.format(
            form.email.data))
        #get the email of the user    
        print("HEYYY",form.email)
        return redirect('/')

    return render_template('login.html', title = 'Sign In', form = form)
    
