from flask import render_template, request, redirect, session, flash
from flask_app import app
from flask_app.models.vehicle_model import Vehicle


# --- REGISTER VEHICLE (RENDER) --- 
@app.route( "/register-vehicle", methods=["GET"] )
def reg_vehicle():
    if "user_id" not in session:
        return redirect( "/" )
    return render_template( "register_vehicle.html")

# --- REGISTER VEHICLE (ACTION) --- 
@app.route( "/vehicle-registered", methods=["POST"])
def vehicle_registered():
    if Vehicle.validate_vehicle( request.form ) == False:
        return redirect( "/register-vehicle" )
    data = {
        **request.form,
        "user_id": session['user_id']
    }
    vehicle_id = Vehicle.register_vehicle(data)
    session["vehicle_id"] = vehicle_id
    return redirect( "/home" )