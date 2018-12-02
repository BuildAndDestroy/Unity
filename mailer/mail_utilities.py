#!/usr/bin/env python
"""Mail library for unity_send_mail script.

Copyright (C) 2018  Mitch O'Donnell devreap1@gmail.com
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.
This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.
You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>
"""

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os.path


class Email(object):
    """Compile an email for sending."""

    def __init__(self, my_email, your_email, subject, text_email_content, html_email_content):
        self.my_email = my_email
        self.your_email = your_email
        self.subject = subject
        self.text_email_content = text_email_content
        self.html_email_content = html_email_content

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

    def __init__(self, username, password, mailserver, my_email, your_email, ssl, email_content):
        self.username = username
        self.password = password
        self.mailserver = mailserver
        self.my_email = my_email
        self.your_email = your_email
        self.ssl = ssl
        self.email_content = email_content

    def test_objects(self):
        """Test user input and verify the content parses."""
        print self.username
        print self.password
        print self.mailserver
        print self.ssl
        print self.email_content

    def connect_send_disconnect(self):
        """Login to a mail server."""
        if self.ssl:
            server = smtplib.SMTP_SSL(self.mailserver, 465)

        else:
            server = smtplib.SMTP(self.mailserver, 25)

        server.login(self.username, self.password)

        if os.path.isfile(self.your_email):
            list_of_emails = []
            with open(self.your_email, 'r') as file_of_emails:
                for email in file_of_emails:
                    list_of_emails.append(email.rstrip())

            for each_email in list_of_emails:
                server.sendmail(self.my_email, each_email, self.email_content.as_string())
        else:
            server.sendmail(self.my_email, self.your_email,
                            self.email_content.as_string())
        server.quit()

        print '[*] Email sent!'
