# Gomerce Backend Service

E-commerce [gomerce](https://github.com/Gomerce/GomerceBE.git) enhanced with JWT authentication, SqlAlchemy, **SQLite** persistence and deployment scripts via Docker. It has all the ready-to-use bare minimum essentials.
This is the backend for and open source ALX-T Udacity full-stack developer graduate project.
It is the backend API for a B2C e-commerce web application

# Collaboration

Our Pledge
In the interest of fostering an open and welcoming environment, we as contributors and maintainers pledge to making participation in our project and our community a harassment-free experience for everyone, regardless of age, body size, disability, ethnicity, gender identity and expression, level of experience, nationality, personal appearance, race, religion, or sexual identity and orientation.

We appreciate your time and effort made to support this project and so we have set out some guidelines to make this community effort worthwhile.

Informations on how best to contribute to this initiative can be found at the [CONTRIBUTING.md](./CONTRIBUTING.md)

# Requirements

```bash
$ git clone https://github.com/Gomerce/GomerceBE.git
$ cd GomerceBE
```
Python 3.9 or higher
PostgreSQL 13.* or higher - recommended
```

# Setup

## Development Environment

Install this extension `Python` from Microsoft on your code editor (VS Code) or it's equivalent for the editor you use, to allow you to use the same coding style with everyone.

1. [Getting Started](#✨-how-to-use-the-code)
2. [Project Structure](#✨-project-structure)
3. [Modules](#✨-api)
4. [Testing](#✨-testing)
5. [Contributors](#✨-contributors)
Setup your linter to follow `pycodestyle` and your formatter to follow `autopep8`

## Virtual environment

How to setup a python virtual environment

- Create the virtual environment,

```bash
$ git clone https://github.com/Gomerce/GomerceBE.git
$ cd GomerceBE
```
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
  SET FLASK_APP=src/server.py
  ```
  - On BASH
  ```
  export FLASK_APP=src/server.py
  ```
  - On POWERSHELL
  ```
  $env:FLASK_APP=src/server.py
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

## ✨ Contributors
> The Gomerce project won't be complete without these backend developers: <br /> 

<img src="https://img.shields.io/github/contributors/gomerce/gomercebe?style=plastic" alt="Contributors" /> <br />

<a href="https://github.com/gomerce/gomercebe/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=gomerce/gomercebe" />
</a>

---
The API Swagger documentation should be accessible at `http://localhost:3303/apidocs`
