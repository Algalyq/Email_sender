import os
from dotenv import load_dotenv
from typing import List
from pydantic import BaseModel

load_dotenv()

SENDER = os.environ.get("EMAIL_SENDER")
PASSWORD = os.environ.get("EMAIL_PASSWORD")


class MailBody(BaseModel):
    to: str
    subject: str
    body: str