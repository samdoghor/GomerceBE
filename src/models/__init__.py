from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from .customer import Customer
from .store import Store
