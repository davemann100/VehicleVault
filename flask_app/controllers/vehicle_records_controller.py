from flask import render_template, request, redirect, session, flash
from flask_app import app
from flask_app.models.vehicle_record_model import Vehicle_Record

# --- NEW SERVICE RECORD (RENDER) --- 
@app.route( "/service-record/new", methods=["GET"] )
def create_service_record():
    if "user_id" not in session:
        return redirect( "/" )
    return render_template( "service_record_new.html" )

# --- NEW SERVICE RECORD (ACTION) --- 
@app.route( "/service-record/submit", methods=["POST"] )
def submit_service_record():
    if "user_id" not in session:
        return redirect( "/" )
    data = {
        **request.form,
        'user_id': session['user_id']
    }
    Vehicle_Record.create_vehicle_record( data )
    return redirect( "/home" )

# --- EDIT ONE RECORD (RENDER) ---
@app.route("/service-record/edit/<int:id>")
def show_one(id):
    this_record = Vehicle_Record.get_one(id)
    return render_template("service_record_edit.html", this_record=this_record)

# --- EDIT ONE RECORD (ACTION) ---
@app.route("/service-record/submit-edit/<int:id>", methods=["POST"])
def update(id):
    data = {
        **request.form,
        'id': id
    }
    Vehicle_Record.update_vehicle_record(data)
    return redirect( "/home" )

# --- DELETE ONE RECORD (ACTION) ---
@app.route("/service-record/delete/<int:id>", methods=["GET"])
def delete(id):
    print("============record deleted=============")
    Vehicle_Record.delete_vehicle_record(id)
    
    return redirect( "/home" )