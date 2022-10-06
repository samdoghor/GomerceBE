# Gomerce Backend Service

This is the backend for and open source ALX-T Udacity full-stack developer graduate project.
It is the backend API for a B2B2C e-commerce web application

# Collaboration

Our Pledge
In the interest of fostering an open and welcoming environment, we as contributors and maintainers pledge to making participation in our project and our community a harassment-free experience for everyone, regardless of age, body size, disability, ethnicity, gender identity and expression, level of experience, nationality, personal appearance, race, religion, or sexual identity and orientation.

We appreciate your time and effort made to support this project and so we have set out some guidelines to make this community effort worthwhile.

Informations on how best to contribute to this initiative can be found at the [CONTRIBUTING.md](./CONTRIBUTING.md)

# Requirements

```
Python 3.9 or higher
PostgreSQL 13.* or higher - recommended
```

# Setup

## Development Environment

Install this extension `Python` from Microsoft on your code editor (VS Code) or it's equivalent for the editor you use, to allow you to use the same coding style with everyone.

Setup your linter to follow `pycodestyle` and your formatter to follow `autopep8`

## Virtual environment

How to setup a python virtual environment

- Create the virtual environment,

  ```
  python -m venv .venv
  ```

- Activate the virtual environment
  - for windows
  ```
  .venv\Scripts\activate
  ```
  - for Linux / macOS
  ```
  source .venv/bin/activate
  ```
- Deactivate the virtual environment when you need to,

  ```
  deactivate
  ```

## Install requirements

For local development

```
pip install -r requirements.txt
```

For production

```
pip install -r requirements-prod.txt
```

## Set environment variables

- Make a copy of the `example.env` file, and rename it to `.env`

- Update the values of the variables in the `.env` file to suite your system environment.

- Create a folder named `logs` in the root directory, if it does not exist

- Create and accout on [Mailjet](https://www.mailjet.com) to get your `API_KEY` and `API_SECRET` for development process.
make sure to validate your `EMAIL_SENDER_EMAIL` on mailjet first

## Datebase setup

### Create databases

Create a Postgres database with the name matching what you have on the `.env` file for `DB_NAME` and `TEST_DB_NAME`. For example:

```
createdb gomerce
createdb gomerce-test
```

### Export your flask app

In order to run your migrations and app using the `flask` command, expose your flask app:

- for Linux / macOS

```
export FLASK_APP=src/server.py
```

- for windows
  - On CMD
  ```
  SET FLASK_APP="src/server.py"
  ```
  - On BASH
  ```
  export FLASK_APP="src/server.py"
  ```
  - On POWERSHELL
  ```
  $env:FLASK_APP="src/server.py"
  ```

### **Create database tables from migrations**

To add the existing database schema and dummy data to your datebase, run:

```
flask db upgrade
```

Make your database changes accessible to others using migrations

```
flask db migrate
```

### **Run server application**

From the root folder, run

```
python src/server.py
```

The application will run at the specified port `APPLICATION_PORT` in `.env` file

The local URL to access the API should be `http://localhost:3303/`

You can visit the Products URL to test the application at `http://localhost:3303/products`

The API Swagger documentation should be accessible at `http://localhost:3303/apidocs`
