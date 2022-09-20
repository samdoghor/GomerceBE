"""
Define the resources for the customer, vendor and admin auth
"""
from flask import jsonify, abort
# from flasgger import swag_from
from flask_restful import Resource
from flask_restful.reqparse import Argument
# from ..repositories import AuthRepository
from utils import parse_params


class AuthResource(Resource):
    """ TODO:methods relative to the authorization """

    @staticmethod
    @parse_params(
        Argument("email", location="json",
                 help="The email of the customer."),
        Argument("password", location="json",
                 help="The password of the customer.")
    )
    # @swag_from("../swagger/auth/login_user.yml")
    def login_user(email, password):
        """ Return a customer key information based on user_id """

        try:
            user = UserRepository.get(user_id=user_id)
            return jsonify({"data": user.json})
        except Exception as e:
            abort(404, e.message)
