import jwt
from functools import wraps
from flask import jsonify, request
from .errors import *
import config
import sys
from repositories import UserRepository


def get_token_auth_header():
    """ Get token from the request header """
    token = None
    if 'x-access-token' in request.headers:
        token = request.headers.get('x-access-token', None)
    if 'Authorization' in request.headers:
        auth = request.headers.get('Authorization', None)
        parts = auth.split()
        if parts[0].lower() != 'bearer':
            raise Unauthorized('Authorization header must start with "Bearer"')
        elif len(parts) == 1:
            raise Unauthorized('Token not found.')
        elif len(parts) > 2:
            raise Unauthorized('Authorization header must be bearer token.')
        token = parts[1]
    if not token:
        raise Unauthorized(
            'Authorization or x-access-token header is expected.')
    return token


def token_required(f):
    """ Verify token for restricted routes"""
    @wraps(f)
    def decorator(*args, **kwargs):
        token = get_token_auth_header()

        try:
            data = jwt.decode(
                token, config.SECRET_KEY, algorithms=["HS256"])
            current_user = UserRepository.get(user_id=data['user_id'])
        except Unauthorized as e:
            return jsonify({'message': e.message}), e.code
        except Exception:
            return jsonify({'message': "Unauthorized"}), 401

        return f(current_user, *args, **kwargs)
    return decorator
