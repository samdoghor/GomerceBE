"""
Defines the blueprint for the auth for admin and customer
"""
from flask import Blueprint

from resources import AuthResource

AUTH_BLUEPRINT = Blueprint("auth", __name__)

AUTH_BLUEPRINT.route("/login-customer", methods=['POST'])(AuthResource.login_user)
AUTH_BLUEPRINT.route("/register-customer", methods=['POST'])(AuthResource.register_user)
