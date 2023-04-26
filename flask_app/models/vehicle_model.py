from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE, EMAIL_REGEX, NAME_REGEX, app
from flask import flash

#create vehicle class for table
#add validation for the form

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

    