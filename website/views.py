
#from flask import Flask

#from werkzeug.utils import redirect 
#from main import app
from flask import render_template, flash, redirect, Blueprint, request
from werkzeug.security import check_password_hash
from wtforms.validators import Email
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

    if request.method == 'POST':
    #Informations from the form
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
            user = User.query.filter_by(email=email).first()

            #Validation process for creating a new user
            if user:
                flash('User already exist', category='error')
            elif len(email) < 3:
                flash('Email is not valid', category='error')
            elif len(password)<5:
                flash('Password is too short', category='error')

            #We create a User
            else:
                newUser = User(firstName = firstName,lastName = lastName,email = email, password_hash = password)
                db.session.add(newUser)
                db.session.commit()
                print(form.firstName, form.lastName)
                return redirect('/')
    return render_template('registration.html', title = 'Register', form = form)

@views.route('/login', methods=['GET', 'POST'])
def login():
    #passing the login form model
    form = LoginForm()
    if form.validate_on_submit() :

        if request.method =='POST':
            email = request.form.get('email')
            password = request.form.get('password_hash')

            user = User.query.filter_by(email=email).first()
            print(user)

            if user:
                if check_password_hash(user.password_hash, password):
                    flash('Logged in successfully!', category='succes')
                else:
                    flash('Loggin did not succeed', category='error')

            else:
                flash('User does not exist', category='error')
            
            return redirect('/')

    return render_template('login.html', title = 'Sign In', form = form)
    
