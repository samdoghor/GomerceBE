""" Defines the Customer repository """
import sys
from sqlalchemy import or_, and_
from models import Customer
from utils.errors import DataNotFound, DuplicateData, InternalServerError
from sqlalchemy.exc import IntegrityError, DataError


class CustomerRepository:
    """ The repository for the customer model """

    @staticmethod
    def get(customer_id=None, username=None, email=None):
        """ Query a customer by customer_id """

        # make sure one of the parameters was passed
        if not customer_id and not username and not email:
            raise DataNotFound(f"Customer not found, no detail provided")

        try:
            query = Customer.query
            if customer_id:
                query = query.filter(Customer.id == customer_id)
            if username:
                query = query.filter(or_(Customer.username == username, Customer.email == username))
            if email:
                query = query.filter(or_(Customer.email == email, Customer.username == email))

            customer = query.first()
            return customer
        except:
            print(sys.exc_info())
            raise DataNotFound(f"Customer with {customer_id} not found")

    @staticmethod
    def getAll():
        """ Query all customers"""
        customers = Customer.query.all()
        all_customers = [customer.json for customer in customers]
        return all_customers

    def update(self, customer_id, **args):
        """ Update a customer's age """
        customer = self.get(customer_id)
        if 'phone' in args and args['phone'] is not None:
            customer.phone = args['phone']

        if 'last_name' in args and args['last_name'] is not None:
            customer.last_name = args['last_name']

        if 'first_name' in args and args['first_name'] is not None:
            customer.first_name = args['first_name']

        return customer.save()

    @staticmethod
    def create(username, last_name, first_name, email, password, phone=None, country=None,
               state=None, city=None, street_name=None, zipcode=None):
        """ Create a new customer """
        try:
            new_customer = Customer(username=username, first_name=first_name, last_name=last_name,
                                    email=email, phone=phone, country=country, state=state, city=city,
                                    street_name=street_name, zipcode=zipcode)
            new_customer.set_password(password)

            return new_customer.save()
        except IntegrityError as e:
            message = e.orig.diag.message_detail
            raise DuplicateData(message)
        except Exception:
            raise InternalServerError
