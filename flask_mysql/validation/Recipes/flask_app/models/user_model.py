from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
from flask import flash
from flask_bcrypt import Bcrypt
from flask_app import app
from flask_app.models.recipe_model import Recipe
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 
bcrypt = Bcrypt(app)

NAME_REGEX = re.compile(r'^[a-zA-Z]+$')

# model the class after the friend table from our database
class User:
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    # Now we use class methods to query our database
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL( DATABASE ).query_db(query)
        # Create an empty list to append our instances of friends
        users = []
         # Iterate over the db results and create instances of friends with cls.
        for user in results:
            users.append( cls(user) )
        return users
    
    @classmethod
    def get_one_by_email_obj(self,data):
        query = "SELECT* FROM users WHERE email = %(email)s;"
        result = connectToMySQL(DATABASE).query_db(query,data)
        return result[0]


    @classmethod
    def create_user(cls,data):
        query = "INSERT INTO users (first_name, last_name, email, password) VALUES(%(first_name)s , %(last_name)s, %(email)s, %(password)s);"
        return connectToMySQL(DATABASE).query_db(query,data)

    @classmethod
    def get_one_by_email(self,data):
        email_exists = False
        query = "SELECT* FROM users WHERE email = %(email)s;"
        result = connectToMySQL(DATABASE).query_db(query,data)
        if result == ():
            return email_exists
        if result[0]['email'] == data['email']:
            email_exists = True
        return email_exists
       

    @classmethod
    def get_password_by_email(self,data):
        query = "SELECT * FROM users WHERE email = %(email)s"
        result = connectToMySQL(DATABASE).query_db(query,data)
        return result[0]['password']

    @classmethod
    def get_recipes_by_user(self, data):
        query = "SELECT * FROM users LEFT JOIN recipes ON users.id = recipes.user_id WHERE users.id = %(id)s"
        result = connectToMySQL(DATABASE).query_db(query,data)
        recipes = []
        
        for recipe in result:
            recipes.append(Recipe(recipe))
        print("********************",recipes)
        return recipes



# **************STATIC METHODS***********************
    @staticmethod
    def validate_user(user_info):
        is_valid = True
        if len(user_info['first_name']) < 2:
            flash("First name must be atleast 2 characters!" , 'first_name')
            is_valid = False
        if not NAME_REGEX.match(user_info['first_name']):
            flash ("Name can only contain alphabetical characters", 'fname_characters')
            is_valid = False
        if not NAME_REGEX.match(user_info['last_name']):
            flash ("Name can only contain alphabetical characters", 'lname_characters')
            is_valid = False
        if len(user_info['last_name']) < 2:
            flash("Last name must be atleast 2 characters.", 'last_name')
            is_valid = False
        if len(user_info['confirm_password']) < 8:
            flash ("Password must be at least 8 characters long!", 'password_length')
            is_valid = False
        if bcrypt.check_password_hash(user_info['password'], user_info['confirm_password']) == False:
            flash("Passwords must match!", 'password_match')
            is_valid = False
        if not EMAIL_REGEX.match(user_info['email']):
            flash("Invalid email address!", 'email_format')
            is_valid = False
        if User.get_one_by_email(user_info) == True:
            flash("This email already is registered to another user", 'email')
            is_valid = False
        return is_valid

    @staticmethod 
    def validate_login(user_info):
        is_valid = True
        if User.get_one_by_email(user_info) == False:
            flash ("Your password/email were entered incorrectly!", 'login')
            is_valid = False
            return is_valid
        password = User.get_password_by_email(user_info)
        if bcrypt.check_password_hash(password,user_info['password']) == False:
            is_valid = False
            flash ("Your password/email were entered incorrectly!", 'login')
            return is_valid
        return is_valid

