import base64
import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def send_email(subject, body, mimeType):
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
            print("Email sent")
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

    print(f"Result: {result}")
    return result


def handler(event, context):
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
