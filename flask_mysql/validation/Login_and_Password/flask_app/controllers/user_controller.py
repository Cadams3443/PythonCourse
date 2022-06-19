from atexit import register
from flask_app.models.user_model import User
from flask_app import app
from flask import render_template, redirect, request, session
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)


@app.route("/")
@app.route("/register")
def display_registration():
    return render_template("index.html")


@app.route("/create/user", methods=['POST'])
def create_user():
    pw_hash = bcrypt.generate_password_hash(request.form['password'])
   
    data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email'],
        'password': pw_hash,
        'confirm_password' : request.form['confirm_password']
    }


    if User.validate_user(data) == False:
        return redirect('/register')
    else:
        session['user_email'] = request.form['email']
        User.create_user(data)
    return redirect("/welcome")


@app.route('/login', methods=["POST"])
def user_login():
    if User.validate_login(request.form) == False:
        return redirect('/register')
    else:
        session['user_email'] = request.form['email']
        return redirect("/welcome")


@app.route('/welcome')
def display_dashboard():
    if session:
        return render_template('user_dashboard.html')
    return redirect ('register')


@app.route('/logout', methods=["POST"])
def user_logout():
    session.clear()
    return redirect('/register')