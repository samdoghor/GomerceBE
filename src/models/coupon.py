"""
Define the Coupon model
"""
from . import db
from .abc import BaseModel, MetaBaseModel
from datetime import datetime


class Coupon(db.Model, BaseModel, metaclass=MetaBaseModel):
    """ The Coupon model """

    __tablename__ = "coupons"

    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(20), nullable=False, unique=True)
    amount = db.Column(db.Float, nullable=False)
    expires_at = db.Column(db.DateTime(), default=datetime.utcnow, nullable=False)
    created_at = db.Column(db.DateTime(), default=datetime.utcnow, nullable=False)
    updated_at = db.Column(db.DateTime(), default=datetime.utcnow)

    #Relationship
    orders = db.relationship("Order", backref="coupons", lazy=True)
