
from flask import Flask
from werkzeug.utils import redirect 
from app import app
from flask import render_template, flash, redirect

from app.models.forms import LoginForm




@app.route("/")
# define the view using a function, which returns a string
def hello_world(name =None):
    return render_template('index.html', name = name)

@app.route('/reg')
def register():
    return render_template('registration.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    #passing the login form model
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}'.format(
            form.email.data))
        
        return redirect('/')

    return render_template('login.html', title = 'Sign In', form = form)
    
if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=5000)