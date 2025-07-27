from schedule import every, repeat, run_pending
from main import main
from smtplib import SMTP
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import time
import asyncio
import sys


def load_email_config():
    config= {}
    with open('config/mail_config.txt', 'r') as file:
        for line in file:
            key, value = line.strip().split('=')
            config[key] = value
    return config


def send_email(report):
    config = load_email_config()
    subject = "Daily Web Crawler Report"
    sender = config['email']
    pw = config['pw']
    to = config['email']
    msg = MIMEMultipart()
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = to

    body = MIMEText(report, 'plain')
    msg.attach(body)

    server = SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender, pw)
    server.send_message(msg)
    server.quit()

#@repeat(every().day.at("10:30"))
# For TESTINGS below:
@repeat(every(30).seconds)
def scheduler():
    sys.argv = ["main.py", "https://news.ycombinator.com/", "3", "25"]
    report = asyncio.run(main())
    send_email(report)

while True:
    run_pending()
    time.sleep(1800)
