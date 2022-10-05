import sys


class InternalServerError(Exception):
    def __init__(self):
        self.code = 500
        self.message = "Internal server error"
        print(sys.exc_info())


class DuplicateData(Exception):
    def __init__(self, message):
        self.code = 400
        self.message = message
        print(sys.exc_info())


class Unauthorized(Exception):
    def __init__(self, message) -> None:
        self.code = 401
        self.message = message


class AccessDenied(Exception):
    def __init__(self, message) -> None:
        self.code = 403
        self.message = message


class DataNotFound(Exception):
    def __init__(self, message) -> None:
        self.code = 404
        self.message = message


class ResourceNotCreated(Exception):
    def __init__(self, message) -> None:
        self.code = 500
        self.message = message


class NotificationFailed(Exception):
    def __init__(self, message) -> None:
        self.code = 500
        self.message = message


errors = {
    "InternalServerError": {
        "message": "Something went wrong",
        "status": 500
    },
    "SchemaValidationError": {
        "message": "Request is missing required fields",
        "status": 400
    },
    "UserNotFound": {
        "message": "User with given name already exists",
        "status": 400
    },
    "UpdatingMovieError": {
        "message": "Updating movie added by other is forbidden",
        "status": 403
    },
    "DeletingMovieError": {
        "message": "Deleting movie added by other is forbidden",
        "status": 403
    },
    "MovieNotExistsError": {
        "message": "Movie with given id doesn't exists",
        "status": 400
    },
    "EmailAlreadyExistsError": {
        "message": "User with given email address already exists",
        "status": 400
    },
    "UnauthorizedError": {
        "message": "Invalid username or password",
        "status": 401
    }
}
