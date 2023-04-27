from flask import render_template, request, redirect, session, flash
from flask_app import app
from flask_app.models.vehicle_record_model import Vehicle_Record

# --- NEW SERVICE RECORD (RENDER) --- 
@app.route( "/service-record/new", methods=["GET"] )
def create_service_record():
    if "user_id" not in session:
        return redirect( "/" )
    return render_template( "service_record_new.html")