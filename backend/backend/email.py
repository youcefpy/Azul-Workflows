import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from backend.models import Customer
from backend.config import settings


def customer_email(customer: Customer) -> str:
    body = f"""
    Hi {customer.name},

    Thank you for getting in touch with us!

    We're excited to learn more about your needs and how our freelance team can support your goals. 
    One of our team members will be reaching out to you shortly to discuss your request in more detail.

    If this message was sent in error, you can safely ignore it.

    ────────────────
    Submitted Details:
    Name: {customer.name}
    Email: {customer.email}
    Phone: {customer.phone_number or 'N/A'}
    Company: {customer.company_name or 'N/A'}
    Service Interest: {customer.service_interest or 'N/A'}
    Message: {customer.message}
    ────────────────

    Best regards,
    AzulWorkFlows
    """
    return body


def admin_email(customer: Customer) -> str:
    body = f"""
    A new customer has submitted a request:

    Name: {customer.name}
    Email: {customer.email}
    Phone: {customer.phone_number or 'N/A'}
    Company: {customer.company_name or 'N/A'}
    Service Interest: {customer.service_interest or 'N/A'}
    Message: {customer.message}
    """
    return body


def send_email_notification(customer: Customer, is_customer: bool) -> None:
    print(f"- Sending email to {customer.email}...")

    msg = MIMEMultipart()
    msg['From'] = settings.SMTP_USERNAME

    if is_customer:
        msg['Subject'] = "Your AzulWorkFlows Request Has Been Received"
        msg['To'] = customer.email
        body = customer_email(customer)
    else:
        msg['Subject'] = f"New Customer: {customer.name}"
        msg['To'] = settings.ADMIN_EMAIL
        body = admin_email(customer)

    msg.attach(MIMEText(body, 'plain'))

    try:
        with smtplib.SMTP(settings.SMTP_SERVER, settings.SMTP_PORT) as server:
            server.starttls()
            server.login(settings.SMTP_USERNAME, settings.SMTP_PASSWORD)
            server.send_message(msg)
        if is_customer:
            print(f"- Email sent to \"{customer.email}\".")
        else:
            print(f"- Email sent to admin.")
    except Exception as e:
        print("Error sending email:", e)