# AUTHOR: ISMAIL MIKOU
# TITLE: AirlineManagementSystem - FINAL PROJECT
# COURSE: CMPSC-363- Intro to Database Systems.
# Professor: J. Xu.


from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100),unique=True,nullable=False)
    firstName = db.Column(db.String(50),nullable=False)
    lastName = db.Column(db.String(50),nullable=False)
    dateOfBirth = db.Column(db.Date,nullable=False)
    password = db.Column(db.String(300))
    def get_id(self):
           return (self.id)


class Aircraft(db.Model):
    aircraft_id = db.Column(db.Integer, primary_key=True)
    Make = db.Column(db.String(45))
    Model = db.Column(db.String(45))
    DateBought = db.Column(db.Date)
    price = db.Column(db.Integer)
    Range = db.Column(db.Integer)
    minRunway = db.Column(db.Integer)
    ServiceCeiling = db.Column(db.Integer)
    speed = db.Column(db.Integer)
    Consumption = db.Column(db.Integer)
    CO2Emission = db.Column(db.Integer)
    ACheckPrice = db.Column(db.Integer)
    ACheckHours = db.Column(db.Integer)

class Airports(db.Model):
    code = db.Column(db.String(3), primary_key=True)
    Continent = db.Column(db.String(45), nullable=False)
    country = db.Column(db.String(45), nullable=False)
    city = db.Column(db.String(45), nullable=False)
    timezone = db.Column(db.Integer)

class Routes(db.Model):
    routeID = db.Column(db.String(6), primary_key=True, nullable=False)
    aircraft_id = db.Column(db.Integer, nullable=False)
    origin = db.Column(db.String(3), nullable=False)
    destination = db.Column(db.String(6), nullable=False)
    distance = db.Column(db.Integer, nullable=False)
    duration = db.Column(db.Time, nullable=False)
    departure = db.Column(db.Time, nullable=False)
    base_price = db.Column(db.Integer, nullable=False)

class Flights(db.Model):
    flightID = db.Column(db.String(6), primary_key=True)
    date = db.Column(db.Date, nullable=False)
    routeID = db.Column(db.String(6), nullable=False)
    aircraftID_F = db.Column(db.Integer, nullable = False)

class Bookings(db.Model):
    BookingNumber = db.Column(db.Integer, primary_key=True)
    FlightNumber = db.Column(db.String(6), nullable = False)
    PassengerID = db.Column(db.Integer, nullable = False)
    FirstName = db.Column(db.String(45),nullable = False)
    LastName = db.Column(db.String(45),nullable = False)
    gender = db.Column(db.String(1), nullable=False)
    dob = db.Column(db.Date, nullable=False)
    Address = db.Column(db.String(100), nullable=False)
    class_ = db.Column(db.String(1),nullable=False)
    CarryOnBag = db.Column(db.Integer, nullable=False)
    CheckingBag = db.Column(db.Integer, nullable=False)
    Insurance = db.Column(db.Integer, nullable=False)
    SpecialMealType = db.Column(db.String(2))

class Payements(db.Model):
    BookingNumber = db.Column(db.Integer,nullable = False, unique=True)
    PayementConfirmation = db.Column(db.String(15),primary_key=True,nullable = False, unique=True )
    PayementMethod = db.Column(db.String(2), nullable = False)
    PayementDate = db.Column(db.Date, nullable = False)
    CardType = db.Column(db.String(2))
    CardNumber = db.Column(db.Integer)

