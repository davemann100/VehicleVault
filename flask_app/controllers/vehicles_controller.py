from flask import render_template, request, redirect, session, flash
from flask_app import app
from flask_app.models.vehicle_model import Vehicle

# --- REGISTER VEHICLE (RENDER) --- 
@app.route( "/register-vehicle", methods=["GET"] )
def reg_vehicle():
    if "user_id" not in session:
        return redirect( "/" )
    return render_template( "register_vehicle.html")