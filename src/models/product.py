"""
Define the Product model
"""

from . import db
from .abc import BaseModel, MetaBaseModel
from datetime import datetime

from sqlalchemy import ForeignKey

class Product(db.Model, BaseModel, metaclass=MetaBaseModel):
    """ The Product model """

    __tablename__ = "products"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(300), nullable=False)
    price = db.Column(db.Float(10,2), nullable=False)
    quantity = db.Column(db.Integer)
    short_desc = db.Column(db.String(500), nullable=False)
    long_desc = db.Column(db.Text())
    rating = db.Column(db.Integer)
    thumbnail = db.Column(db.String(100))
    image = db.Column(db.String(100))
    created_at = db.Column(db.DateTime(), default=datetime.utcnow)
    updated_at = db.Column(db.DateTime(), default=datetime.utcnow)

    #Foreign Key
    sellers_id = db.Column(db.Integer, db.ForeignKey('sellers.id'), nullable=False)
    product_categories_id = db.Column(db.Integer, db.ForeignKey('product_categories.id'), nullable=False)

    #Relationship
    reviews = db.relationship('Review', backref='products', lazy=True)
    order_details = db.relationship('Order_Detail', backref='products', lazy=True)