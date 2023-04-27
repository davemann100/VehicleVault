from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE, NAME_REGEX, app
from flask import flash

class Vehicle:
    def __init__( self, data ):
        self.id = data['id']
        self.year = data['year']
        self.make = data['make']
        self.model = data['model']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']

    # --- INSERT VEHICLE ---
    @classmethod
    def register_vehicle( cls, data ):
        query  = "INSERT INTO vehicle ( year_made, make, model, user_id) "
        query += "VALUES( %(year_made)s, %(make)s, %(model)s, %(user_id)s);"
        result = connectToMySQL( DATABASE ).query_db( query, data )
        print("---Vehicle Registered---")
        return result

    # --- VALIDATE VEHICLE REGISTRATION ---
    @staticmethod
    def validate_vehicle( data ):
        is_valid = True
        if int(data["year_made"]) < 1886:
            flash( "Enter a valid year", "error_year" )
            is_valid = False
        if not NAME_REGEX.match( data["make"] ):
            flash( "Letters only", "error_make" )
            is_valid = False
        if len( data["make"] ) < 2:
            flash( "Minimum 2 characters", "error_make" )
            is_valid = False
        if len( data["model"] ) < 2:
            flash( "Minimum 2 characters", "error_model" )
            is_valid = False
        return is_valid