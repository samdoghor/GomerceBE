from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from .customer import Customer
from .paymentMethod import paymentMethod
from .verification_token import VerificationToken
from .product import Product

