from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import encoders
import smtplib

import os

import config


def send_email(
    recipients: list[str],
    mail_body: str,
    mail_subject: str,
    attachment: str = None,
):
    TOKEN = config.TOKEN_UKR_NET
    USER = config.USER
    SMTP_SERVER = config.SMTP_SERVER

    msg = MIMEMultipart('alternative')
    msg['Subject'] = mail_subject
    msg['From'] = f'<Email was sent from {USER}>'
    msg['To'] = ', '.join(recipients)
    msg['Reply-To'] = USER
    msg['Return-Path'] = USER
    msg['X-Mailer'] = 'decorator'

    # text_to_send = MIMEText(mail_body, 'plain')
    text_to_send = MIMEText(mail_body, 'html')
    msg.attach(text_to_send)

    if attachment:
        is_file_exists = os.path.exists(attachment)
        if is_file_exists:
            basename = os.path.basename(attachment)
            filesize = os.path.getsize(attachment)
            file = MIMEBase('application', f'octet-stream; name={basename}')
            file.set_payload(open(attachment, 'br').read())
            file.add_header('Content-Description', attachment)
            file.add_header(
                'Content-Description',
                f'attachment; filename={attachment}, size={filesize}',
            )
            encoders.encode_base64(file)
            msg.attach(file)

    mail = smtplib.SMTP_SSL(SMTP_SERVER)
    mail.login(USER, TOKEN)
    mail.sendmail(USER, recipients, msg.as_string())
    mail.quit()


send_email(['test_hillel_api_mailing@ukr.net'], '<h1>mail body22</h1>', 'mail subject', 'README.md')
