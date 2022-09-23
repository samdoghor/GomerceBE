"""
Define the OrderDetails model
"""
from . import db
from .abc import BaseModel, MetaBaseModel


class order_details(db.Model, BaseModel, metaclass=MetaBaseModel):
    """Order details Model"""

    __tablename__ = "order_details"

    id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.Boolean, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    sku = db.Column(db.String(50), nullable=False)

    #foreign keys
    # order_id = db.Column(db.Integer, db.ForeignKey('order.id'), nullable=False)
    # product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
