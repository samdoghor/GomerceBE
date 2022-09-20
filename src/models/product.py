"""
Define the Product model
"""

from . import db
from .abc import BaseModel, MetaBaseModel
from datetime import datetime

from sqlalchemy import ForeignKey
#from models.seller import Seller
#from models.product_categories import Product_Category

class Product(db.Model, BaseModel, metaclass=MetaBaseModel):
    """ The Product model """

    __tablename__ = "products"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(300), nullable=False)
    price = db.Column(db.Float(10,2), nullable=False)
    stock = db.Column(db.Integer)
    short_desc = db.Column(db.String(500), nullable=False)
    long_desc = db.Column(db.Text())
    rating = db.Column(db.Integer)
    thumbnail = db.Column(db.String(100))
    image = db.Column(db.String(100))
    created_at = db.Column(db.DateTime(), default=datetime.utcnow)
    updated_at = db.Column(db.DateTime(), default=datetime.utcnow)

    #Foreign Key
    #sellers_id = db.Column(db.Integer, ForeignKey(Seller.id), nullable=False)
    #product_categories_id = db.Column(db.Integer, ForeignKey(Product_Category.id), nullable=False)

    #Relationship
    reviews = db.relationship('Review', backref='Product', lazy='dynamic')
    order_details = db.relationship('Order_Details', backref='Product', lazy='dynamic')
