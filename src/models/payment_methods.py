"""
Define the Payment Methods model
"""
from . import db
from .abc import BaseModel, MetaBaseModel
from datetime import datetime



class PaymentMethods(db.Model, BaseModel, metaclass=MetaBaseModel):
    """ The Payment Methods model """

    __tablename__ = "paymentMethods"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    currency = db.Column(db.String(32), nullable=False)
    created_at = db.Column(db.DateTime(), default=datetime.utcnow)
    updated_at = db.Column(db.DateTime(), default=datetime.utcnow)

    #Relationship
    payment_details = db.relationship('paymentDetails', backref='paymentMethods', lazy=True)