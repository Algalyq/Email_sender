# main.py
import logging
from fastapi import FastAPI
from configs.config import MailBody
from smtp.mailer import send_mail
from email.message import EmailMessage
import ssl 
import smtplib

app = FastAPI()

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

@app.get("/")
async def index():
    return {"status": "fastapi mailserver is running."}

@app.post("/send-email")
async def schedule_mail(req: MailBody):
    try:
        send_mail(req)
        logger.info(f"Email sent successfully to {req.to}")
        return {"status": "ok"}
    except Exception as e:
        logger.error(f"Error sending email: {str(e)}")
        return {"status": "error", "error_message": str(e)}
