"""
Define the Customer model
"""


from datetime import datetime
from uuid import uuid4

from sqlalchemy import UUID

from werkzeug.security import check_password_hash, generate_password_hash

from . import db
from .abc import BaseModel, MetaBaseModel
from validators.jwt import encode_auth_token


class Customer(db.Model, BaseModel, metaclass=MetaBaseModel):
    """ The Customer model """

    __tablename__ = "customers"

    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    username = db.Column(db.String(32), nullable=False, unique=True)
    first_name = db.Column(db.String(300))
    last_name = db.Column(db.String(300))
    email = db.Column(db.String(100), nullable=False, unique=True)
    phone = db.Column(db.String(15))
    password = db.Column(db.Text(), nullable=False)
    country = db.Column(db.String(50))
    state = db.Column(db.String(70))
    city = db.Column(db.String(50))
    street_name = db.Column(db.String(50))
    zipcode = db.Column(db.String(50))

    created_at = db.Column(db.DateTime(), default=datetime.utcnow)
    updated_at = db.Column(db.DateTime(), onupdate=datetime.utcnow)

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def encode_token(self, id, first_name, last_name):
        return encode_auth_token(id, first_name, last_name)

    # Relationship
    orders = db.relationship('Order', backref='customers', lazy=True)
    carts = db.relationship('Cart', backref='customers', lazy=True)
