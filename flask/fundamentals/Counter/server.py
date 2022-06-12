from flask import Flask, render_template, request,redirect,session

app = Flask(__name__)

app.secret_key = 'secretkey' # set a secret key for security purposes


@app.route("/")
def render_home():
    session['num'] += 1
   
    return render_template("index.html")

@app.route("/destroy", methods=["POST"])
def reset_count():
    session['num'] = 0
    return redirect("/")


@app.route("/count", methods=['POST'])
def two_count():
    session['num'] += 2
    return redirect("/count",)   

@app.route("/count") 
def display_count():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug = True)