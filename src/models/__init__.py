from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from .customer import Customer
from .orderdetails import order_details

