from flask_app.config.mysqlconnect import connectToMySQL
from flask_app import DATABASE
from flask_app.models import ninja_model

# model the class after the friend table from our database
class Dojo:
    def __init__( self , data ):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    # Now we use class methods to query our database
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL( DATABASE ).query_db(query)
        # Create an empty list to append our instances of friends
        dojos = []
         # Iterate over the db results and create instances of friends with cls.
        for dojo in results:
            dojos.append( cls(dojo) )
        return dojos

    @classmethod
    def create_dojo(cls,data):
        query = "INSERT INTO dojos (name) VALUES(%(name)s);"
        return connectToMySQL(DATABASE).query_db(query,data)

    @classmethod
    def get_one(cls,data):
        query = "SELECT* from dojos WHERE id = %(id)s;"
        result = connectToMySQL(DATABASE).query_db(query,data)
        return cls(result[0])

    @classmethod
    def get_dojo_ninjas(cls,data):
        query = "SELECT * from dojos LEFT JOIN ninjas ON dojos.id = ninjas.dojo_id WHERE dojos.id = %(id)s;"
        result = connectToMySQL(DATABASE).query_db(query,data)
        ninjas = []
        for ninja in result:
            ninjas.append(ninja_model.Ninja(ninja))
        return ninjas