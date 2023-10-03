from configs.config import *
import smtplib
import ssl
from email.message import EmailMessage

def send_mail(data: dict | None = None):
    email = EmailMessage()
    email["From"] = SENDER
    email["To"] = data.to
    email["Subject"] = data.subject
    

    email.set_content(data.body)

    smtp_server = "smtp.gmail.com"
    smtp_port = 465

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, smtp_port, context=context) as server:
        server.login(SENDER, PASSWORD)
        server.send_message(email)
        return True
    return False
