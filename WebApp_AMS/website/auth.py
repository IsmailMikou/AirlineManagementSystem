# AUTHOR: ISMAIL MIKOU
# TITLE: AirlineManagementSystem - FINAL PROJECT
# COURSE: CMPSC-363- Intro to Database Systems.
# Professor: J. Xu.

from flask import Blueprint,render_template, request, flash, redirect, url_for
from .models import User
from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_mysqldb import MySQL
from flask_login import login_user, login_required, logout_user, current_user
import random

auth = Blueprint('auth',__name__)

@auth.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Logged in Successfully!', category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash('Incorrect password!', category='error')
        else:
            flash('Email Does not exist.', category='error')
    return render_template("login.html", user=current_user)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

@auth.route('/sign-up', methods=['GET','POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        firstName = request.form.get('firstName')
        lastName = request.form.get('lastName')
        dateOfBirth = request.form.get('dateOfBirth')
        password1 = request.form.get('password1')
        password2  = request.form.get('password2')

        user = User.query.filter_by(email=email).first()
        if user:
            flash('Email Already exists', category='error')

        if len(email) < 10:
            flash('Email must be greater than 10 CHARACTERS.', category='error')
        elif len(firstName) < 2:
            flash('First name must be greater than 2 CHARACTERS.', category='error')
        elif len(lastName) < 2:
            flash('Last name must be greater than 2 CHARACTERS.', category='error')
        elif len(dateOfBirth) != 10:
            flash('Date of Birth FORMAT is not YYYY-MM-DD.', category='error')
        elif len(password1) < 7:
            flash('Password should be at leat 8 Characters.', category='error')
        elif password1 != password2:
            flash('Passwords not Matching.', category='error')
        else:
            #add user to Database
            new_user = User(id = random.randrange(100000000,999999999),email=email, firstName=firstName,lastName=lastName,dateOfBirth=dateOfBirth,password=generate_password_hash(password1,method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            login_user(user, remember=True)
            flash('Account successfully created!', category='success')
            return redirect(url_for('views.home'))
            

    return render_template("sign_up.html", user=current_user)
