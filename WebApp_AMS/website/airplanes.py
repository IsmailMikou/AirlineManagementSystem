# AUTHOR: ISMAIL MIKOU
# TITLE: AirlineManagementSystem - FINAL PROJECT
# COURSE: CMPSC-363- Intro to Database Systems.
# Professor: J. Xu.


from flask import Blueprint,render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_mysqldb import MySQL
from flask_login import login_user, login_required, logout_user, current_user
import random


airplanes = Blueprint('airplanes',__name__)
airplanes = Blueprint('airplanes',__name__)
airplanes = Blueprint('airplanes',__name__)
