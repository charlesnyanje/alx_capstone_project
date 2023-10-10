from flaskblog import app
from flask import render_template
from flaskblog.forms import LoginForm, RegistrationForm





@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html',)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    return render_template('register.html', title='Register', form=form)