"""
Define the paymentMethod model
"""
from locale import currency
from . import db
from datetime import datetime
from sqlalchemy_utils import CurrencyType, Currency


class paymentMethod(db.Model):
    __tablename__ = 'payment_methods'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    currency = db.Column(CurrencyType)
    created_at = db.Column(db.DateTime(), default = datetime.utcnow)
    updated_at = db.Column(db.DateTime(), default = datetime.utcnow)


def __init__(self, name='',currency=''):
    self.name = name
    self.currency = currency


payment = paymentMethod()
payment.currency = Currency('NGN')

# db.session.add(payment)
# db.session.commit()

payment.currency # Currency('NGN')
payment.currency.name # Nigerian Naira