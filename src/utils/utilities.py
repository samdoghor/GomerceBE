""" Define some common functions """
import secrets


def generate_token(length):
    """ Generates an alphanumerical token for the specified length"""
    return secrets.token_hex(length)
