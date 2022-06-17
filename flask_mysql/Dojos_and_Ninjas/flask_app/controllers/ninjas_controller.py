from flask_app import app
from flask import render_template, redirect, request
from flask_app.models.ninja_model import Ninja
from flask_app.models.dojo_model import Dojo


@app.route("/add/ninja")
def display_add_ninja():
    all_dojos = Dojo.get_all()
    return render_template("ninjas.html", all_dojos = all_dojos)

@app.route("/add/ninjas", methods = ['POST'])
def create_ninja():
    data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'age':request.form['age'],
        'dojo_id':request.form['dojo_id']
    }
    num = request.form['dojo_id']
    Ninja.create_ninja(data)
    return redirect(f'/dojo/{num}')