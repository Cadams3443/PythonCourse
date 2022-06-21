from flask import Flask
DATABASE = "recipe_schema"




app = Flask(__name__)

app.secret_key = "secret"