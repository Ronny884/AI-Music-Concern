import re
import asyncio
import imaplib
import email
from asyncio import sleep
from email.header import decode_header
from config.config_reader import settings


class IMAPClient:
    def __init__(self):
        self.imap_server = "imap.gmail.com"
        self.imap_port = 993
        self.username = settings.MAIL_USERNAME
        self.password = settings.MAIL_PASSWORD
        self.connection = None

    def connect(self):
        self.connection = imaplib.IMAP4_SSL(self.imap_server, self.imap_port)
        self.connection.login(self.username, self.password)

    async def fetch_unread_emails(self, folder="inbox"):
        self.connection.select(folder)
        result, data = self.connection.search(None, 'UNSEEN')
        email_ids = data[0].split()
        emails = []

        for email_id in email_ids:
            result, message_data = self.connection.fetch(email_id, '(RFC822)')
            raw_email = message_data[0][1]
            email_message = email.message_from_bytes(raw_email)
            emails.append(email_message)

        return emails

    async def fetch_all_emails_from_sender(self, sender_email, folder="inbox"):
        self.connection.select(folder)
        result, data = self.connection.search(None, f'(FROM "{sender_email}")')
        email_ids = data[0].split()
        emails = []

        for email_id in email_ids:
            result, message_data = self.connection.fetch(email_id, '(RFC822)')
            raw_email = message_data[0][1]
            email_message = email.message_from_bytes(raw_email)
            emails.append(email_message)

        return emails

    def close(self):
        self.connection.close()
        self.connection.logout()


async def main():
    client = IMAPClient()
    client.connect()
    while True:
        await sleep(10)
        unread_emails = await client.fetch_unread_emails()
        for email_message in unread_emails:
            sender_email = re.search(r'[\w\.-]+@[\w\.-]+', email_message['From']).group(0)

            print(f"New message from: {sender_email}")
            print(f"Subject: {email_message['Subject']}")
            print(f"Date: {email_message['Date']}")
            print("Fetching entire conversation...")

