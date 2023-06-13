"""
licdata/rest/infrastructure/aws_lambda/mail.py

This file provides some utilities for sending emails.

Copyright (C) 2023-today ACM S.L. Licdata

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""
import base64
import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from typing import Dict


def send_email(subject: str, body: str, mimeType: str) -> bool:
    """
    Sends an email.
    :param subject: The subject of the email.
    :type subject: str
    :param body: The body of the email.
    :type body: str
    :param mimeType: The mime-type of the email.
    :type mimeType: str
    :return: True if the email is sent.
    :rtype: bool
    """
    try:
        mailFrom = os.environ["MAIL_FROM"]
        mailTo = os.environ["MAIL_TO"]
        bcc = os.environ["MAIL_BCC"]
        rcpt = bcc.split(",") + [mailTo]
        msg = MIMEMultipart("alternative")
        msg["Subject"] = subject
        msg["To"] = mailTo
        msg.attach(MIMEText(body, mimeType))
        try:
            server = smtplib.SMTP(
                os.environ["AWS_SES_SMTP_HOST"],
                os.environ["AWS_SES_SMTP_PORT"],
                os.environ["AWS_SES_SMTP_TIMEOUT"],
            )
            server.ehlo()
            server.starttls()
            server.login(
                os.environ["AWS_SES_SMTP_USERNAME"], os.environ["AWS_SES_SMTP_PASSWORD"]
            )
            server.sendmail(mailFrom, rcpt, msg.as_string())
            server.quit()
            result = True
        except BaseException as inst:
            print(type(inst))
            print(inst.args)
            print(inst)
            result = False
        except:
            print("Unknown error")
            result = False

    except BaseException as err:
        print(type(err))
        print(err.args)
        print(err)
        result = False

    return result


def handler(event -> Dict, context) -> Dict:
    """
    Handler hook used to send emails.
    :param event: The event to handle.
    :type event: Dict
    :param context: The AWS Lambda context.
    :type context: object
    :return: The SMTP response.
    :rtype: smtplib.Response
    """
    body = str(event.get("body", ""))
    print(body)
    if body:
        try:
            body = base64.b64decode(body).decode("utf-8")
        except BaseException as inst:
            print(type(inst))
            print(inst.args)
            print(inst)
            print("body not in base64")

    print(f"Sending email with {body}")
    send_email("Mail endpoint", body, "plain")

    response = {"headers": {"Content-Type": "application/json"}}
    response["statusCode"] = 200

    return response
