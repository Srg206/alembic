from email.message import EmailMessage
import random
import smtplib
from dotenv import load_dotenv, find_dotenv
import os

load_dotenv(find_dotenv())

SMTP_HOST = os.getenv("SMTP_HOST")
SMTP_PORT = os.getenv("SMTP_PORT")
SMTP_SENDER=os.getenv("SMTP_SENDER")
SMTP_PASS=os.getenv("SMTP_PASS")


Codes_db={}

def Send_verification_number(receiver_email):
    try:
        email = EmailMessage()
        email['Subject'] = str(generate_number(receiver_email))
        email['From'] = SMTP_SENDER
        email['To'] ="Srg206.32@gmail.com"
        with smtplib.SMTP_SSL(SMTP_HOST, SMTP_PORT) as server:
            print(SMTP_SENDER)
            print(SMTP_PASS)
            server.login(SMTP_SENDER, SMTP_PASS)
            server.send_message(email)
    except Exception as e:
        print(e)

def generate_number(email:str):
    a= random.randint(10000,99999)
    Codes_db[email]=a
    return a


Send_verification_number("messenger.SMTtp@yandex.ru")
    