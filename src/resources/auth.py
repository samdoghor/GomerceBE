"""
Define the resources for the customer, vendor and admin auth
"""
import sys

from flask import jsonify, abort
from flasgger import swag_from
from flask_restful import Resource
from flask_restful.reqparse import Argument
from repositories import CustomerRepository, VerificationTokenRepository
from utils import parse_params, Notification
from utils.errors import DataNotFound, DuplicateData


class AuthResource(Resource):
    """ methods relative to the authorization """

    @staticmethod
    @parse_params(
        Argument("username", location="json",
                 help="The username/email of the customer."),
        Argument("password", location="json",
                 help="The password of the customer.")
    )
    @swag_from("../swagger/auth/login_customer.yml")
    def login_user(username, password):
        """ Login a customer annd return basic information if customer exists """

        try:
            customer = CustomerRepository.get(username=username)
            print(customer)
            if not customer.check_password(password):
                abort(401, "Username or Password is incorrect")
            return jsonify({"data": customer.json})
        except DataNotFound:
            abort(401, "Username or Password is incorrect")
        except:
            abort(500)

    @staticmethod
    @parse_params(
        Argument("email", required=True, location="json",
                 help="The email of the customer."),
        Argument("username", required=True, location="json",
                 help="The username of the customer."),
        Argument("password", required=True, location="json",
                 help="The password of the customer."),
        Argument("first_name", required=True, location="json",
                 help="The first_name of the customer."),
        Argument("last_name", required=True, location="json",
                 help="The last_name of the customer."),
        Argument("confirm_url", required=True, location="json",
                 help="The url for email confrimation"),
        Argument("phone", location="json"),
    )
    @swag_from("../swagger/auth/register_customer.yml")
    def register_user(email, password, username, first_name, last_name, confirm_url, phone=None):
        """ Register a customer and return the information of customer """

        # TODO: validate inputs very well
        try:
            # customer = CustomerRepository.create(email=email, password=password, username=username,
            #                                      first_name=first_name, last_name=last_name,
            #                                      phone=phone)

            customer = CustomerRepository.get(customer_id=26)
            # create verification tokens for the email and phone
            email_token = VerificationTokenRepository.create(user_id=customer.id,
                                                             user_type="customer", email=True,
                                                             phone=False)

            # create email template for verification token
            email_confirm_url = f"{confirm_url}/{email_token}"
            email_notification = Notification(email=True)
            email_message = email_notification.create_email_template("user_verification_email.html",
                                                                     confirm_url=email_confirm_url,
                                                                     customer=customer)

            # send email verification notification
            recipient = {
                "name": f"{customer.first_name} {customer.last_name}",
                "email": customer.email
            }
            subject = "Customer Email Verification"
            Notification.send_email(message=email_message, to=recipient, subject=subject)

            return jsonify({"data": customer.json})
        except DuplicateData as e:
            abort(e.code, e.message)
        except Exception as e:
            print(sys.exc_info())
            abort(500, e)
