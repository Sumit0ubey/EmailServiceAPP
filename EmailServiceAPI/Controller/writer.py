from logging import INFO, StreamHandler, basicConfig, info, error, exception
from smtplib import SMTP, SMTPException
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from .templates import Amazing, cool, simple, custom, packagesPlan, registrationEmail, tokenRevert

basicConfig(
    level=INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        StreamHandler()
    ]
)


def get_smtp_config(email: str) -> tuple[str, int]:
    domain = email.lower().split("@")[-1]

    smtp_settings = {
        "gmail.com": ("smtp.gmail.com", 587),
        "yahoo.com": ("smtp.mail.yahoo.com", 587),
        "outlook.com": ("smtp.office365.com", 587),
        "icloud.com": ("smtp.mail.me.com", 587),
        "zoho.com": ("smtp.zoho.com", 587),
        "yandex.com": ("smtp.yandex.com", 587),
        "mail.com": ("smtp.mail.com", 587),
    }

    return smtp_settings.get(domain, ("smtp." + domain, 587))


def setMailServer(email: str, password: str) -> SMTP:
    service, port = get_smtp_config(email)
    try:
        server = SMTP(service, port)
        server.ehlo()
        server.starttls()
        server.login(email, password)
        info(f"Connected to SMTP server: {service}:{port}")
        return server
    except SMTPException as e:
        error(f"SMTP connection failed for {email}: {e}")
        raise


def createMail(_from: str, _to: str, subject: str, data: str) -> MIMEMultipart:
    message = MIMEMultipart()
    message["From"] = _from
    message["To"] = _to
    message["Subject"] = subject
    message.attach(MIMEText(data, "html"))
    return message


def sendMail(username: str, password: str, _to: str, subject: str, data: str, template_id: int = 0,
             company_name: str = None, company_link: str = None, email_title: str = None, iD: int = None, token: str = None) -> bool:
    try:
        with setMailServer(username, password) as server:
            html_data = ""
            if template_id == 1:
                html_data += cool(data=data, company_name=company_name)
            elif template_id == 2:
                html_data += Amazing(data=data, company_name=company_name)
            elif template_id == 3:
                html_data += custom(data=data, subject=email_title, company_name=company_name, company_link=company_link)
            elif template_id == 4:
                html_data += packagesPlan()
            elif template_id == 5:
                html_data += registrationEmail(iD=iD, token=token)
            elif template_id == 6:
                html_data += tokenRevert(token=token)
            else:
                html_data += simple(data=data)

            message = createMail(username, _to, subject, html_data)
            server.sendmail(username, _to, message.as_string())
            info(f"Email sent successfully to {_to}")
            return True
    except SMTPException as e:
        error(f"Failed to send email: {e}")
        return False
    except Exception as e:
        exception(f"Unexpected error: {e}")
        return False
