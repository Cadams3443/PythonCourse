from flask import Flask
DATABASE = "user_login_schema"




app = Flask(__name__)

app.secret_key = "secret"