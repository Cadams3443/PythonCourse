import re
from flask import Flask, render_template, request,redirect,session

app = Flask(__name__)
app.secret_key = "secret"



@app.route("/")
def display_home():
    return render_template("index.html")

@app.route("/process", methods = ["POST"])
def go_to_result():

    # new_result = {'name' : eureurejr, 'dojolocal' : Seattle, 'favlang' : Mandarin} 
        # If a check box is unchecked, thre is no key pair made.

    # Form -> Fill in Data -> Submit Data gives defined values to associated names via request.form['name']
    # If a checkbox is unchecked, it is not going to define that checkbox as a variable.

    # request.form['fun'] => We are assuming 'fun' is valid and has a value before checking. If this is not declared, it blows the &%$# up. (bad key error)    
    # request.form.get('fun') => Does not need this to be declared, 
    #                            and instead takes in a value from the "value" attribute by default.
    #                            For example if it is an unchecked box it returns "None" rather than erroring out.

    # Good Google-Fu example: Flask request.form radio button if selected
    if request.form.get('fun') and request.form.get('not_robot') :
        session['new_result'] = {
            "name_entry": request.form["name_entry"],
            "dojolocal": request.form["dojolocal"],
            "favlang": request.form["favlang"],
            "comment_entry": request.form["comment_entry"],
            "not_robot": request.form['not_robot'],
            "fun": request.form['fun']
        }
    elif request.form.get('fun'):
        session['new_result'] = {
            "name_entry": request.form["name_entry"],
            "dojolocal": request.form["dojolocal"],
            "favlang": request.form["favlang"],
            "comment_entry": request.form["comment_entry"],
            "not_robot": "some string",
            "fun":request.form['fun']
        }
    elif  request.form.get('not_robot'):
        session['new_result'] = {
            "name_entry": request.form["name_entry"],
            "dojolocal": request.form["dojolocal"],
            "favlang": request.form["favlang"],
            "comment_entry": request.form["comment_entry"],
            "not_robot": request.form['not_robot'],
            "fun":"I am not having fun anymore :( "
        }
    else:
          session['new_result'] = {
            "name_entry": request.form["name_entry"],
            "dojolocal": request.form["dojolocal"],
            "favlang": request.form["favlang"],
            "comment_entry": request.form["comment_entry"],
            "not_robot": "string",
            "fun":"some string"
        }
    return redirect("/result")

@app.route("/result")
def display_result():
    return render_template("result.html")


if __name__ == "__main__":
    app.run(debug = True)


