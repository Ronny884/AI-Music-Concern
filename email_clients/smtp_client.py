import asyncio
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from config.config_reader import settings


class SMTPClient:
    def __init__(self):
        self.smtp_server = "smtp.gmail.com"
        self.smtp_port = 587
        self.username = settings.MAIL_USERNAME
        self.password = settings.MAIL_PASSWORD

    async def send_email(self, subject, to_email, text=None, from_email=None,
                         audio_file=None, video_file=None, html_content=None):
        from_email = from_email or self.username
        msg = MIMEMultipart()
        msg['From'] = f"GoodAI <{from_email}>"
        msg['To'] = to_email
        msg['Subject'] = subject

        if text is not None:
            msg.attach(MIMEText(text, 'plain'))

        # Прикрепление HTML-контента
        if html_content:
            msg.attach(MIMEText(html_content, 'html'))

        # Прикрепление файла
        if audio_file:
            part = MIMEBase('application', 'octet-stream')
            part.set_payload(open(audio_file, 'rb').read())
            encoders.encode_base64(part)
            part.add_header('Content-Disposition', 'attachment; filename="%s"' % audio_file)
            msg.attach(part)

        if video_file:
            part = MIMEBase('application', 'octet-stream')
            part.set_payload(open(video_file, 'rb').read())
            encoders.encode_base64(part)
            part.add_header('Content-Disposition', 'attachment; filename="%s"' % video_file)
            msg.attach(part)

        with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
            server.starttls()
            server.login(self.username, self.password)
            server.send_message(msg)


async def send(company_name, email, text=None, audio_file=None, video_file=None, html_content=None):
    subject = f"A song for {company_name} by GoodAI"
    to_email = email
    client = SMTPClient()
    await client.send_email(subject, to_email,
                            from_email=settings.MAIL_USERNAME,
                            text=text,
                            audio_file=audio_file,
                            video_file=video_file,
                            html_content=html_content)


