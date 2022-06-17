from flask_app import app
from flask import render_template, redirect, request
from flask_app.models.dojo_model import Dojo
from flask_app.models.ninja_model import Ninja

@app.route('/')
@app.route('/dojos')
def display_dojos():
    all_dojos = Dojo.get_all()
    return render_template('dojo.html',all_dojos = all_dojos)

@app.route("/add/dojo", methods =['POST'])
def create_dojo():
    Dojo.create_dojo(request.form)
    return redirect("/dojos")

@app.route("/dojo/<int:id>")
def display_dojo_info(id):
    data = {
        "id":id
    }
    dojo = Dojo.get_one(data)
    all_ninjas = Dojo.get_dojo_ninjas(data)
    return render_template("dojo_show.html", dojo = dojo, all_ninjas=all_ninjas)