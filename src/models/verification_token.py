"""
Define the VerificationToken model
"""
from sqlalchemy import event
from . import db
from .abc import BaseModel, MetaBaseModel
from datetime import datetime


class VerificationToken(db.Model, BaseModel, metaclass=MetaBaseModel):
    """ The VerificationToken model """

    __tablename__ = "verification_tokens"

    id = db.Column(db.Integer, primary_key=True)
    token = db.Column(db.String(200), nullable=False)
    used_status = db.Column(db.Boolean, nullable=False, default=False)
    user_id = db.Column(db.Integer, nullable=False)
    user_type = db.Column(db.String(70), nullable=False)
    email_token = db.Column(db.Boolean, nullable=False, default=False)
    phone_token = db.Column(db.Boolean, nullable=False, default=False)
    expires_at = db.Column(db.DateTime(), nullable=False)
    created_at = db.Column(db.DateTime(), default=datetime.utcnow)
    updated_at = db.Column(db.DateTime(), default=datetime.utcnow)


@event.listens_for(VerificationToken, 'before_update')
def pre_update_actions(target, value, initiator):
    print(target, value, initiator)
