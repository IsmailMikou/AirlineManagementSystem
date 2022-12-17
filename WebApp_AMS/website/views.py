# AUTHOR: ISMAIL MIKOU
# TITLE: AirlineManagementSystem - FINAL PROJECT
# COURSE: CMPSC-363- Intro to Database Systems.
# Professor: J. Xu.


from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from . import db
from flask import redirect, url_for
from .models import Aircraft, Airports, Routes, Flights, Bookings, Payements
from . import db

views = Blueprint('views',__name__)

@views.route('/')
@login_required
def home():
    return render_template("home.html", user=current_user)

@views.route('/update_data', methods=['POST'])
@login_required
def update_data():
  # Access the form data
  aircraft_id = request.form['toUpdate']
  field_to_update = request.form['dropdown2']
  new_data = request.form['update']

  # Query the database to get the aircraft with the specified ID
  aircraft = Aircraft.query.get(aircraft_id)
  
  # Update the relevant field in the aircraft object
  if field_to_update == "option1":
    aircraft.make = new_data
  elif field_to_update == "option2":
    aircraft.model = new_data
  # Add additional elif statements for other fields as needed
  
  # Commit the updates to the database
  db.session.commit()

  # Return a success message or redirect the user to a new page
  flash("Aircraft updated successfully")
  return redirect(url_for('views.airplane'))


@views.route('/airplanes/<int:aircraft_id>')
@login_required
def delete_aircraft(id):
  airplanes = Aircraft.query.all()
  aircraft_to_delete = Aircraft.query.get_or_404(id)
  try:
    db.session.delete(aircraft_to_delete)
    db.session.commit()
    flash("Aircraft Deleted Successfully")
    return render_template("aircraft.html", user=current_user, airplanes=airplanes)
  except:
    flash("Problem happened while deleting Aircraft")
    return render_template("aircraft.html", user=current_user, airplanes=airplanes)


@views.route('/airplanes',methods=['GET','POST'])
@login_required
def airplane():
  airplanes = Aircraft.query.all()
  return render_template("aircraft.html", user=current_user, airplanes=airplanes)


@views.route('/airports',methods=['GET','POST'])
@login_required
def airport():
  airports = Airports.query.all()
  return render_template("airports.html", user=current_user, airports=airports)


@views.route('/routes',methods=['GET','POST'])
@login_required
def route():
  routes = Routes.query.all()
  return render_template("routes.html", user=current_user, routes=routes)


@views.route('/flights',methods=['GET','POST'])
@login_required
def flight():
  flights = Flights.query.all()
  return render_template("flights.html", user=current_user, flights=flights)



@views.route('/bookings',methods=['GET','POST'])
@login_required
def booking():
  bookings = Bookings.query.all()
  return render_template("bookings.html", user=current_user, bookings=bookings)



@views.route('/payements',methods=['GET','POST'])
@login_required
def payement():
  payements = Payements.query.all()
  return render_template("payements.html", user=current_user, payements=payements)


