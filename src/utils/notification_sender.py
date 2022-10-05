""" Email or/and SMS notification sender"""
from jinja2 import Environment, FileSystemLoader, select_autoescape

from config import EMAIL_SENDER_NAME, EMAIL_SENDER_EMAIL
from utils.mail_service import mailjet
from utils.errors import NotificationFailed


class Notification:
    """ Defines notification methods """

    def __init__(self, email=False, sms=False):
        """ initialize notification method"""
        self.email = email
        self.sms = sms
        self.env = None

        if self.email:
            self.env = Environment(
                loader=FileSystemLoader('templates'),
                autoescape=select_autoescape(['html', 'xml'])
            )

    def create_email_template(self, file_name, **kwargs):
        """ creates an email template using a html file """
        template = self.env.get_template(file_name)
        html = template.render(**kwargs)
        return html

    @staticmethod
    def send_email(to, subject, message, sender=None):
        """ Sends email to the 'to' variable"""
        if sender is None:
            sender = {
                'name': EMAIL_SENDER_NAME,
                'email': EMAIL_SENDER_EMAIL,
            }
        # build the mailjet data
        data = {
            'Messages': [
                {
                    "From": {
                        "Email": sender['email'],
                        "Name": sender['name']
                    },
                    "To": [
                        {
                            "Email": to['email'],
                            "Name": to['name']
                        }
                    ],
                    "Subject": subject,
                    "HTMLPart": message
                }
            ]
        }

        result = mailjet(data)
        if result.status_code != 200:
            raise NotificationFailed("Email notification not sent!")

        return result
