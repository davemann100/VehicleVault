from flask import render_template, request, redirect, session, flash
from flask_app import app
from flask_app.models.user_model import User
from flask_app.models.vehicle_record_model import Vehicle_Record


# --- LOG/REG PAGE (RENDER) --- 
@app.route( "/", methods=["GET"] )
def display_login_registration():
    return render_template( "main.html" )

# --- LOGIN PAGE LOGIN (ACTION) ---
@app.route( "/login", methods=["POST"] )
def proccess_login():
    current_user = User.get_one( request.form )     #SELECT in SQL returns a list of rows
    if current_user == None:
        flash( "This email doesn't exist in our DB", "error_login_email" )
        return redirect( "/" )
    if User.validate_password( request.form["password"], current_user.password ) == False:
        return redirect( "/" )
    session["user_id"] = current_user.id
    session["first_name"] = current_user.first_name
    return redirect( "/home" ) 

# --- HOME PAGE (RENDER) ---
@app.route( "/home", methods=["GET"] )
def show_home():
    if "user_id" not in session:
        return redirect( "/" )
    all_records = Vehicle_Record.get_user_records()
    return render_template( "home.html", all_records=all_records)

# --- LOGIN PAGE REGISTER (ACTION) --- 
@app.route( "/user/new", methods=["POST"] )
def create_user():
    if User.validate_reg( request.form ) == False:
        return redirect( "/" )
    encrypted_password = User.encrypt_string( request.form["password"] )
    data = {
        **request.form,
        "password" : encrypted_password
    }
    user_id = User.create_one_user( data )   #INSERT INTO in SQL and return ID of user that registered
    session["user_id"] = user_id        #store their ID in session
    session["first_name"] = request.form["first_name"]
    return redirect( "/register-vehicle" )

# --- LOGOUT BUTTON (ACTION)
@app.route( "/logout", methods=["POST"] )
def process_logout():
    session.clear()
    return redirect( "/" )