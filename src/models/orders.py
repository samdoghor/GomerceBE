
"""
Define the Orders model
"""
from . import db
from .abc import BaseModel, MetaBaseModel
from datetime import datetime
from enum import Enum, unique
from sqlalchemy.dialects.postgresql import ENUM as pgEnum

@unique
class Status(Enum):
    Pending = 'pending'
    Processing = 'processing'
    Completed = 'completed'


class Orders(db.Model, BaseModel, metaclass=MetaBaseModel):
    """ The Orders model """

    __tablename__ = "orders"

    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    modified_at = db.Column(db.DateTime, default=datetime.utcnow)
    total_order_cost = db.Column(db.Float, nullable=False)
    tax = db.Column(db.Float, nullable=False)
    delivery_status = db.Column(db.Boolean, nullable=False, default=False)
    delivery_date = db.Column(db.DateTime, nullable=False)
    status = db.Column(pgEnum(Status), unique=False, nullable=False)
    customer_id = db.Column(db.Integer, db.ForeignKey("customers.id"), nullable=False)
    seller_id = db.Column(db.Integer, db.ForeignKey("sellers.id"), nullable=False)
    coupon_id = db.Column(db.Integer, db.ForeignKey("coupons.id"), nullable=False)
    payment_details = db.relationship("paymentDetails", backref="orders", lazy=True)
    order_details =  db.relationship("orderdetails", backref="orders", lazy=True)


