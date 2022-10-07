"""
Define the Payment Detail model
"""
from . import db
from .abc import BaseModel, MetaBaseModel
from datetime import datetime


class PaymentDetail(db.Model, BaseModel, metaclass=MetaBaseModel):
    """ The Payment Details model """

    __tablename__ = "payment_details"

    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Integer)
    status = db.Column(db.String(10))
    created_at = db.Column(db.DateTime(), default=datetime.utcnow)
    updated_at = db.Column(db.DateTime(), default=datetime.utcnow)
    

    #Foreign Key
    order_id = db.Column(db.Integer, db.ForeignKey('orders.id'), nullable=False)
    payment_method_id = db.Column(db.Integer, db.ForeignKey('payment_methods.id'), nullable=False)    

    #Relationship
    orders = db.relationship('Order', backref='payment_details', lazy=True)