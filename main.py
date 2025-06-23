import smtplib
import os
from dotenv import load_dotenv
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

load_dotenv()


def send_email():
    """
    Connects to the SMTP server and sends a simple email
    using credentials from a .env file.
    """
    # --- Configuration ---

    # SMTP settings
    smtp_server = os.getenv("SMTP_SERVER")
    smtp_port = int(os.getenv("SMTP_PORT"))

    # SMTP credentials
    smtp_username = os.getenv("SMTP_USER")
    smtp_password = os.getenv("SMTP_PASSWORD")

    # Email details
    sender_email = os.getenv("SENDER_EMAIL")
    receiver_email = os.getenv("RECEIVER_EMAIL")

    subject = "Testing email from Python"
    body_html = """
    <html>
      <body>
        <p>This is an <b>HTML</b> email.</p>
      </body>
    </html>
    """

    # --- Validate Configuration ---
    if not all([smtp_server, smtp_port, smtp_username, smtp_password, sender_email, receiver_email]):
        print("Error: Missing one or more environment variables.")
        print(
            "Please check your .env file and ensure it contains SMTP_SERVER, SMTP_PORT, SMTP_USER, SMTP_PASSWORD, SENDER_EMAIL, and RECEIVER_EMAIL.")
        return

    # --- Create the Email Message ---
    msg = MIMEMultipart('alternative')
    msg['Subject'] = subject
    msg['From'] = sender_email
    msg['To'] = receiver_email

    part = MIMEText(body_html, 'html')

    msg.attach(part)

    # --- Send the Email ---
    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(smtp_username, smtp_password)
            server.sendmail(sender_email, receiver_email, msg.as_string())

        print("Email sent successfully!")

    except smtplib.SMTPAuthenticationError:
        print("Authentication failed. Please check your SMTP username and password in the .env file.")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    send_email()
