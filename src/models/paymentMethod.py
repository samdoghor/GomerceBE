"""
Define the paymentMethod model
"""
from locale import currency
from . import db
from sqlalchemy_utils import CurrencyType, Currency


class payment_Method(db.Model):
    __tablename__ = 'paymentMethod'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    currency = db.Column(CurrencyType)


def __init__(self, name='',currency=''):
    self.name = name
    self.currency = currency


payment = payment_Method()
payment.currency = Currency('NGN')
db.session.add(payment)
db.session.commit()

payment.currency # Currency('NGN')
payment.currency.name # Nigerian Naira