"""
Define the resources for the customers
"""
from flask import jsonify, abort
from flasgger import swag_from
from flask_restful import Resource
from flask_restful.reqparse import Argument
from repositories import CustomerRepository
from utils import parse_params
from utils.errors import DataNotFound


class CustomerResource(Resource):
    """ methods relative to the customer """

    @staticmethod
    @swag_from("../swagger/customer/get_one.yml")
    def get_one(customer_id):
        """ Return a customer key information based on customer_id """

        try:
            customer = CustomerRepository.get(customer_id=customer_id)
            return jsonify({"data": customer.json})
        except DataNotFound as e:
            abort(404, e.message)
        except Exception:
            abort(500)

    @staticmethod
    @swag_from("../swagger/customer/get_all.yml")
    def get_all():
        """ Return all customer key information based on the query parameter """
        customers = CustomerRepository.getAll()
        return jsonify({"data": customers})

    @staticmethod
    @parse_params(
        Argument("first_name", location="json",
                 help="The first_name of the customer."),
        Argument("last_name", location="json",
                 help="The last_name of the customer."),
        Argument("age", location="json",
                 help="The age of the customer.")
    )
    # @swag_from("../swagger/customer/PUT.yml")
    def update_customer(customer_id, last_name, first_name, age):
        """ Update a customer based on the provided information """
        print(customer_id)
        repository = CustomerRepository()
        customer = repository.update(
            customer_id=customer_id, last_name=last_name, first_name=first_name, age=age
        )
        return jsonify({"data": customer.json})

    @staticmethod
    @parse_params(
        Argument("first_name", location="json", required=True,
                 help="The first_name of the customer."),
        Argument("last_name", location="json", required=True,
                 help="The last_name of the customer."),
        Argument("age", location="json", required=True,
                 help="The age of the customer.")
    )
    # @swag_from("../swagger/customer/POST.yml")
    def post(last_name, first_name, age):
        """ Create a customer based on the provided information """
        # Check duplicates
        customer = CustomerRepository.create(
            last_name=last_name, first_name=first_name, age=age
        )
        return jsonify({"data": customer.json})
