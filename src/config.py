from dotenv import load_dotenv
import logging
import os
import datetime

load_dotenv()
# Databse configs
DB_NAME = os.getenv("DB_NAME", 'gomerce')
DB_TEST_NAME = os.getenv("DB_TEST_NAME", 'gomerce-test')
DB_USER = os.getenv("DB_USER", 'postgres')
DB_PASSWORD = os.getenv("DB_PASSWORD", '')
DB_HOST = os.getenv("DB_HOST", 'localhost')
DB_PORT = os.getenv("DB_PORT", 5432)

DB_URI = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

# Application configs
SECRET_KEY = os.getenv("SECRET_KEY")
DEBUG = os.getenv("ENVIRONEMENT") == "DEV"
APPLICATION_ROOT = os.getenv("API_APPLICATION_ROOT", "/api")
HOST = os.getenv("APPLICATION_HOST")
PORT = int(os.getenv("APPLICATION_PORT", "3000"))
SQLALCHEMY_TRACK_MODIFICATIONS = False

# Notification configs
EMAIL_API_SECRET = os.getenv("EMAIL_API_KEY", '')
EMAIL_API_KEY = os.getenv("EMAIL_API_SECRET", '')
EMAIL_SENDER_NAME = os.getenv("EMAIL_SENDER_NAME", '')
EMAIL_SENDER_EMAIL = os.getenv("EMAIL_SENDER_EMAIL", '')

if DEBUG:
    logging.basicConfig(
        level=logging.DEBUG,
        format="%(levelname)s: %(message)s",
        datefmt="%d/%m/%y %H:%M:%S",
    )
else:
    filename = datetime.datetime.now().strftime('%d-%m-%Y')
    logging.basicConfig(
        filename=f"logs/{filename}.log",
        level=logging.WARNING,
        format="%(asctime)s %(levelname)s:\
        %(filename)s %(funcName)s \
        pid:%(process)s module:%(module)s %(message)s",
        datefmt="%H:%M:%S",
    )
