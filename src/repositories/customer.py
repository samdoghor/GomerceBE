""" Defines the Customer repository """
from models import Customer
from utils.errors import UserNotFound


class CustomerRepository:
    """ The repository for the customer model """

    @staticmethod
    def get(customer_id):
        """ Query a customer by customer_id """
        customer = Customer.query.filter(Customer.id == customer_id).first()

        if customer is None:
            raise UserNotFound(f"Customer with {customer_id} not found")
        return customer

    @staticmethod
    def getAll():
        """ Query all customers"""
        customers = Customer.query.all()
        all_customers = [customer.json for customer in customers]
        return all_customers

    def update(self, customer_id, **args):
        """ Update a customer's age """
        customer = self.get(customer_id)
        if 'age' in args and args['age'] is not None:
            customer.age = args['age']

        if 'last_name' in args and args['last_name'] is not None:
            customer.last_name = args['last_name']

        if 'first_name' in args and args['first_name'] is not None:
            customer.first_name = args['first_name']

        return customer.save()

    @staticmethod
    def create(last_name, first_name, age):
        """ Create a new customer """
        customer = Customer(last_name=last_name, first_name=first_name, age=age)
        return customer.save()
