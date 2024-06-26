"""
Define the Product Subcategory model
"""

from datetime import datetime
from uuid import uuid4

from sqlalchemy import UUID

from . import db
from .abc import BaseModel, MetaBaseModel


class ProductSubcategory(db.Model, BaseModel, metaclass=MetaBaseModel):
    """ The Product Subcategory model """

    __tablename__ = "product_subcategories"

    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    name = db.Column(db.String(100), nullable=False)
    sku = db.Column(db.String(300), nullable=False)
    created_at = db.Column(db.DateTime(), default=datetime.utcnow)
    updated_at = db.Column(db.DateTime(), onupdate=datetime.utcnow)

    # Foreign Key
    product_categories_id = db.Column(UUID(as_uuid=True), db.ForeignKey(
        'product_categories.id'), nullable=False)

    # Relationship
    products = db.relationship(
        'Product', backref='product_subcategories', lazy=True)
