# AUTHOR: ISMAIL MIKOU
# TITLE: AirlineManagementSystem - FINAL PROJECT
# COURSE: CMPSC-363- Intro to Database Systems.
# Professor: J. Xu.


from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import os
from os import path
db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'AMS'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:2031@localhost/airlinemanagementsystem'

    db.init_app(app)

    from .views import views
    from .auth import auth
    from .airplanes import airplanes


    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    app.register_blueprint(airplanes, url_prefix='/')

    from .models import User, Aircraft

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app
