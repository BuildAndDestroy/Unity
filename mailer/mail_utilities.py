#!/usr/bin/env python
"""

"""

import getpass
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class Email(object):
    """Compile an email for sending."""
    def __init__(self, my_email, your_email, subject, text_email_content, html_email_content):
        self.my_email = my_email
        self.your_email = your_email
        self.subject = subject
        self.text_email_content = text_email_content
        self.html_email_content = html_email_content
        self.email_compiled = self.compile_email

    @property
    def compile_email(self):
        """Create an eamil in text and html format."""
        message = MIMEMultipart('alternative')
        message['Subject'] = self.subject
        message['From'] = self.my_email
        message['To'] = self.your_email
        text = self.text_email_content
        html = self.html_email_content
        text_message = MIMEText(text, 'plain')
        html_message = MIMEText(html, 'html')
        message.attach(text_message)
        message.attach(html_message)
        return message

class SendEmail(object):
    """Manage connecting and disconnecting to a mail server."""
    def __init__(self, username, password, mailserver, my_email, your_email, ssl, list_of_emails):
        self.username = username
        self.password = password
        self.mailserver = mailserver
        self.my_email = my_email
        self.your_email = your_email
        self.ssl = ssl
        self.list_of_emails = list_of_emails

    def test_objects(self):
        print self.username
        print self.password
        print self.mailserver
        print self.ssl
        print self.list_of_emails

    def connect_send_disconnect(self):
        """Login to a mail server."""
        if self.ssl:
            server = smtplib.SMTP_SSL(self.mailserver, 465)

        else:
            server = smtplib.SMTP(self.mailserver, 25)

        server.login(self.username, self.password)

        #for email_content in self.list_of_emails:
            #server.sendmail(my_email, your_email, email_content.as_string())
        server.sendmail(self.my_email, self.your_email, self.list_of_emails.as_string())

        server.quit()


        