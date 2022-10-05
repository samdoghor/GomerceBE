""" Mailjet Email service"""

import os
from mailjet_rest import Client

from config import EMAIL_API_SECRET, EMAIL_API_KEY


def mailjet(data):
    mailjet_client = Client(auth=(EMAIL_API_KEY, EMAIL_API_KEY), version='v3.1')

    """ Dummy data for format
    data = {
        'Messages': [
            {
                "From": {
                    "Email": "<a verified email on mailjet>",
                    "Name": "MaryBlessing"
                },
                "To": [
                    {
                        "Email": "<recipient email>",
                        "Name": "MaryBlessing"
                    }
                ],
                "Subject": "Greetings from Mailjet.",
                "TextPart": "My first Mailjet email",
                "HTMLPart": "<h3>Dear passenger 1, welcome to <a href='https://www.mailjet.com/'>Mailjet</a>!</h3><br />May the delivery force be with you!"
            }
        ]
    }
    """

    return mailjet_client.send.create(data=data)
    # print(result.status_code)
    # print(result.json())
