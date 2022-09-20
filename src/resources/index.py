"""
Define the REST verbs relative to the index route
"""
from flasgger import swag_from
from flask.json import jsonify
from flask_restful import Resource


class IndexResource(Resource):
    """ Verbs relative to the index route """

    @staticmethod
    @swag_from("../swagger/index.yml")
    def get():
        """ Return a message for the customer accessing the home """
        return jsonify({"message": "Welcome to Gomerce API"})
