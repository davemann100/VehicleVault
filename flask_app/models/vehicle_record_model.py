from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE, EMAIL_REGEX, NAME_REGEX, app
from flask import flash

class Vehicle_Record:
    def __init__( self, data ):
        self.id = data['id']
        self.date = data['date']
        self.title = data['title']
        self.description = data['description']
        self.mileage = data['mileage']
        self.price = data['price']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']