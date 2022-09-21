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
    coupon_code = db.Column(db.Integer, nullable=False, unique=True)
    coupon_amount = db.Column(db.Float, nullable=False)
    coupon_expiring_date = db.Column(db.DateTime(), nullable=False)
    orders = db.relationship("orders", backref="coupons", lazy=True)
