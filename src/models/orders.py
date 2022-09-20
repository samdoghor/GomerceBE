
"""
Define the Orders model
"""
from . import db
from .abc import BaseModel, MetaBaseModel
from datetime import datetime
from enum import Enum


class Status(Enum):
    Pending = 'pending'
    Processing = 'processing'
    Completed = 'completed'


class Orders(db.Model, BaseModel, metaclass=MetaBaseModel):
    """ The Orders model """

    __tablename__ = "orders"

    id = db.Column(db.Integer, primary_key=True)
    start_time = db.Column(db.DateTime, nullable=False, default="2035-04-15 20:00:00")
    artist_id = db.Column(db.Integer, db.ForeignKey("Artist.id"), nullable=False)
    venue_id = db.Column(db.Integer, db.ForeignKey("Venue.id"), nullable=False)


