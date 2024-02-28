from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

#The UserMixin will add Flask-Login attributes to the model so that Flask-Login will be able to work with it.
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    email = db.Column(db.String(100), unique=True)
    name = db.Column(db.String(1000))
    password = db.Column(db.String(100))