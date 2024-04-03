import logging
import smtplib
import imaplib

EMAIL_TITLE = ''
EMAIL_WAS_SENT = ''
AUTHENTICATION_FAILURE = ''
WRONG_PARAMETER_TYPE = ''


class EmailSender:
    def __init__(self, email_type: int, sender_email: str, sender_email_password: str, receiver_email: str,
                 temporary_password: str, receiver_name: str = None) -> None:
        self.email_type = email_type
        self.sender_email = sender_email
        self.sender_email_password = sender_email_password
        self.receiver_name = receiver_name
        self.temporary_password = temporary_password
        self.receiver_email = receiver_email

    def prepare_and_send_email(self) -> None:
        email_text = self._prepare_email_data()
        self._send_email(email_text)

    def _prepare_email_data(self) -> str:
        return f'First Name: {self.receiver_name}\nPassword: {self.temporary_password}'

    def _send_email(self, email_text: str) -> None:
        try:
            server = smtplib.SMTP_SSL('smtp.gmail.com')
            server.ehlo()
            server.login(self.sender_email, self.sender_email_password)
            server.sendmail(self.sender_email, self.receiver_email, email_text)
            server.close()
        except imaplib.IMAP4.error:
            logging.error(AUTHENTICATION_FAILURE)
