"""
Defines the welcome page for the users
"""
from flask import Blueprint
from resources import IndexResource

INDEX_BLUEPRINT = Blueprint("/", __name__)
INDEX_BLUEPRINT.route("", methods=['GET'])(IndexResource.get)
