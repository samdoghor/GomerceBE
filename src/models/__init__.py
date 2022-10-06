from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from .customer import Customer
<<<<<<< HEAD
from .paymentMethod import paymentMethod
=======
from .verification_token import VerificationToken
from .product import Product
>>>>>>> b0876a7bff72364ceaf8fdb37c1cbb4397879318
