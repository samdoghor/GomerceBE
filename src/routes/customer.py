"""
Defines the blueprint for the customers
"""
from flask import Blueprint

from resources import CustomerResource

CUSTOMER_BLUEPRINT = Blueprint("customer", __name__)

CUSTOMER_BLUEPRINT.route(
    "/customers", methods=['GET'])(CustomerResource.get_all)
CUSTOMER_BLUEPRINT.route("/customers", methods=['POST'])(CustomerResource.post)
CUSTOMER_BLUEPRINT.route("/customers/<int:customer_id>",
                         methods=['GET'])(CustomerResource.get_one)
