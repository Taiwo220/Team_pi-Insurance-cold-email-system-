import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import asyncio
import aiosmtplib


async def send_email(recipient: str, subject: str, body: str):
    # Read SMTP settings from environment variables
    smtp_host = os.environ.get("SMTP_HOST")  # e.g., "smtp.gmail.com"
    smtp_port = int(os.environ.get("SMTP_PORT"))  # e.g., 465
    smtp_username = os.environ.get("SMTP_USERNAME")  # e.g., "your_email@gmail.com"
    smtp_password = os.environ.get("SMTP_PASSWORD")  # e.g., "your_email_password_or_app_password"

    # Create the email
    msg = MIMEMultipart()
    msg["From"] = smtp_username
    msg["To"] = recipient
    msg["Subject"] = subject
    msg.attach(MIMEText(body, "plain"))

    # Send the email in a separate thread
    loop = asyncio.get_event_loop()
    try:
        await loop.run_in_executor(
            None,  # None means use the default ThreadPoolExecutor
            _send_email_sync,  # The synchronous function to run
            smtp_host, smtp_port, smtp_username, smtp_password, msg
        )
        print("Email sent successfully!")
    except Exception as e:
        print(f"Error sending email: {e}")
        raise

async def send_email(recipient: str, subject: str, body: str):
    # Read SMTP settings from environment variables
    smtp_host = os.environ.get("SMTP_HOST")  # e.g., "smtp.gmail.com"
    smtp_port = int(os.environ.get("SMTP_PORT"))  # e.g., 465
    smtp_username = os.environ.get("SMTP_USERNAME")  # e.g., "your_email@gmail.com"
    smtp_password = os.environ.get("SMTP_PASSWORD")  # e.g., "your_email_password_or_app_password"

    # Create the email
    msg = MIMEMultipart()
    msg["From"] = smtp_username
    msg["To"] = recipient
    msg["Subject"] = subject
    msg.attach(MIMEText(body, "plain"))

    # Log the recipient's email address
    print(f"Sending email to: {recipient}")

    # Send the email
    try:
        await aiosmtplib.send(
            msg,
            hostname=smtp_host,
            port=smtp_port,
            username=smtp_username,
            password=smtp_password,
            use_tls=True,
        )
        print("Email sent successfully!")
    except Exception as e:
        print(f"Error sending email: {e}")
        raise