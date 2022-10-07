"""
Define the Store model
"""

from email.policy import default
from . import db
from .abc import BaseModel, MetaBaseModel
from datetime import datetime

from werkzeug.security import generate_password_hash, check_password_hash



class Store(db.Model, BaseModel, metaclass=MetaBaseModel):
     """"
     The Store Model
     """

     __tablename__ = "stores"

     id = db.Column(db.Integer, primary_key=True)
     name = db.Column(db.String(50), nullable=False, unique=True)
     address = db.Column(db.String)
     phone = db.Column(db.String(15))
     email = db.Column(db.String(100))
     created_at = db.Column(db.DateTime(), default=datetime.utcnow)
     updated_at = db.Column(db.DateTime(), default=datetime.utcnow)
     email_verified = db.Column(db.Boolean, default=False)
     phone_verified = db.Column(db.Boolean, default=False)


     #Relationship
     sellers = db.relationship('Seller', backref='stores', lazy=True)