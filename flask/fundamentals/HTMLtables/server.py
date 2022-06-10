from flask import Flask, render_template

app = Flask(__name__)


users = [
   {'first_name' : 'Michael', 'last_name' : 'Choi'},
   {'first_name' : 'John', 'last_name' : 'Supsupin'},
   {'first_name' : 'Mark', 'last_name' : 'Guillen'},
   {'first_name' : 'KB', 'last_name' : 'Tonel'}
]



@app.route("/")
def test():
    return render_template("index.html", first_name = "first_name", last_name = "last_name", users=users)



if __name__ == "__main__":
    app.run(debug = True)