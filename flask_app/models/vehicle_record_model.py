from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE, EMAIL_REGEX, NAME_REGEX, app
from flask import flash, session

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

    # --- INSERT VEHICLE RECORD ---
    @classmethod
    def create_vehicle_record( cls, data ):
        query  = """INSERT INTO vehicle_records ( date, title, description, mileage, price, user_id)
                VALUES( %(date)s, %(title)s, %(description)s, %(mileage)s, %(price)s, %(user_id)s);
                """
        result = connectToMySQL( DATABASE ).query_db( query, data )
        return result
    
    # --- GRAB ALL RECORDS --
    @classmethod
    def get_user_records( cls ):
        query = "SELECT * FROM vehicle_records "
        query += "WHERE user_id = "
        query += str(session["user_id"] )
        results = connectToMySQL(DATABASE).query_db(query)
        #instantiate data coming back from select query
        record_instances = []
        for row in results:
            this_record = cls(row)
            record_instances.append(this_record)
        return record_instances
    
    # --- GRAB ONE RECORD ---
    @classmethod
    def get_one( cls, record_id ):
        data = {
            'id': record_id
        }
        query = """SELECT * FROM vehicle_records
                WHERE id = %(id)s"""
        results = connectToMySQL(DATABASE).query_db(query,data)
        return cls(results[0])
    
    # --- UPDATE ONE RECORD ---
    @classmethod
    def update_vehicle_record( cls, data ):
        query = """
                UPDATE vehicle_records
                SET date = %(date)s, title = %(title)s, description = %(description)s, mileage = %(mileage)s, price = %(price)s
                WHERE id = %(id)s;
                """
        return connectToMySQL(DATABASE).query_db(query,data)
    
    # --- DELETE ONE RECORD ---
    @classmethod
    def delete_vehicle_record( cls, record_id ):
        query = """DELETE FROM vehicle_records
                WHERE id = %(id)s;"""
        data = {'id': record_id}
        return connectToMySQL(DATABASE).query_db(query,data)