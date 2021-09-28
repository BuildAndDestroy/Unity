#!/usr/bin/env python3
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

import glob
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class Email(object):
    """Compile an email for sending."""

    def __init__(self, my_email, my_display_name, your_email, subject, html_email_file) -> None:
        self.my_email = my_email
        self.my_display_name = my_display_name
        self.your_email = your_email
        self.subject = subject
        self.html_email_file = html_email_file

    def full_path_file(self) -> list:
        """If file not found, raise an exception."""
        full_file_path = glob.glob(f'{self.html_email_file}', recursive=False)
        if not full_file_path:
            raise ValueError("File not found!")
        return full_file_path

    def read_html_file(self) -> str:
        """Read a file and return the content in memory"""
        html_email_file = self.full_path_file()
        with open(html_email_file[0], 'r') as html_file:
            read_file_html = html_file.read()
        return read_file_html

    #@property
    def compile_email(self, your_email) -> str:
        """Create an email in html format."""
        message = MIMEMultipart('alternative')
        message['Subject'] = self.subject
        message['From'] = f'{self.my_display_name} {self.my_email}'
        message['To'] = your_email
        html = self.read_html_file()
        html_message = MIMEText(html, 'html')
        message.attach(html_message)
        return message


class SendEmail(Email):
    """Manage connecting and disconnecting to a mail server."""

    def __init__(self, my_email, my_display_name, your_email, subject, html_email_file, username, password, mailserver, ssl) -> None:
        super().__init__(my_email, my_display_name, your_email, subject, html_email_file)
        self.username = username
        self.password = password
        self.mailserver = mailserver
        self.ssl = ssl

    def test_objects(self) -> None:
        """Test user input and verify the content parses."""
        print(self.username)
        print(self.password)
        print(self.mailserver)
        print(self.ssl)
        print(self.email_content)

    def username_is_file(self) -> bool:
        """Check if username is string or file."""
        full_file_path = glob.glob(f'{self.your_email}', recursive=False)
        if full_file_path:
            return True
        return False

    def list_of_emails(self) -> list:
        """Open a file full of email addresses and return as a list."""
        full_file_path = glob.glob(f'{self.your_email}', recursive=False)
        with open(full_file_path[0], 'r') as file_of_emails:
            all_user_emails = file_of_emails.readlines()
            all_user_emails = [line.rstrip() for line in all_user_emails]
        return all_user_emails

    def connect_send_disconnect(self) -> None:
        """Login to a mail server."""
        if self.ssl:
            server = smtplib.SMTP_SSL(self.mailserver, 465)

        if not self.ssl:
            server = smtplib.SMTP(self.mailserver, 25)

        server.login(self.username, self.password)

        if self.username_is_file():
            for index in self.list_of_emails():
                compiled_email = super().compile_email(index)
                server.sendmail(self.my_email, index, compiled_email.as_string())
                print(f'[*] Email sent to {index}!')
        else:
            compiled_email = super().compile_email(self.your_email)
            server.sendmail(self.my_email, self.your_email,
                            compiled_email.as_string())
            print(f'[*] Email sent to {self.your_email}!')
        server.quit()
