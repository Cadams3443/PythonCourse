from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
from flask import flash
from flask_app import app

# model the class after the friend table from our database
class Recipe:
    def __init__( self , data ):
        self.id = data['id']
        self.name = data['name']
        self.description = data['description']
        self.instructions = data['instructions']
        self.time = data['time']
        self.date_made = data['date_made']
        self.user_id = data['user_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    # Now we use class methods to query our database

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM recipes;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL( DATABASE ).query_db(query)
        # Create an empty list to append our instances of friends
        recipes = []
         # Iterate over the db results and create instances of friends with cls.
        for recipe in results:
            recipes.append( cls(recipe) )
        return recipes

    @classmethod
    def delete_recipe(self,data):
        query = "DELETE FROM recipes WHERE id = %(id)s"
        return connectToMySQL(DATABASE).query_db(query, data)

    @classmethod
    def get_one_by_id(self,data):
        query = "SELECT * FROM recipes WHERE id =%(id)s"
        result = connectToMySQL(DATABASE).query_db(query, data)
        return result[0]

    @classmethod
    def create_recipe(self,data):
        query = "INSERT INTO recipes(name, description, instructions, time, date_made, user_id) Values(%(name)s, %(description)s , %(instructions)s, %(time)s , %(date_made)s, %(user_id)s); "
        return connectToMySQL(DATABASE).query_db(query, data)

    @classmethod
    def edit_recipe(self,data):
        query = "UPDATE recipes SET name = %(name)s, description = %(description)s, instructions = %(instructions)s, date_made = %(date_made)s, time =%(time)s WHERE id = %(id)s"
        result = connectToMySQL(DATABASE).query_db(query,data)
        return result

    @staticmethod
    def validate_recipe(recipe_info):
        is_valid = True
        if len(recipe_info['name']) < 3:
            flash("Recipe name must be atleast 3 characters!" , 'recipe_name')
            is_valid = False
        if len(recipe_info['description']) < 3:
            flash("Recipe description must be atleast 3 characters!" , 'recipe_description')
            is_valid = False
        if len(recipe_info['instructions']) < 3:
            flash("Recipe name must be atleast 3 characters!" , 'recipe_instructions')
            is_valid = False
        return is_valid
