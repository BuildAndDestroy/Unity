#!/usr/bin/env python
"""Script to create an email and send through external mailserver.

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

import argparse
import getpass

from mailer.mail_utilities import Email, SendEmail


def parse_arguments():
    """Accept user input, also create the help menu."""
    legal_statement = '[*] unity_send_mail Copyright (C) 2018 Mitch O\'Donnell\n    This program comes with ABSOLUTELY NO WARRANTY.\n    This is free software, and you are welcome to redistribute it\nunder certain conditions.'
    url = '[*] https://github.com/BuildAndDestroy/Unity'
    epilog = '{}\n\n{}'.format(url, legal_statement)
    parser = argparse.ArgumentParser(
        description=__doc__, epilog=epilog, formatter_class=argparse.RawTextHelpFormatter)

    # subparsers = parser.add_subparsers(help='commands', dest='commands')

    # single_mailer = subparsers.add_parser(
    #     'spear_fish', help='Send a single email.')
    parser.add_argument(
        'my_email', help='The email address you will be sending from as yourself.')
    # parser.add_argument(
    #     'your_email', help='The email address you will be sending to, the recipient.')
    parser.add_argument(
        'mailserver', help='The mailserver we will connect to to send our email.')
    parser.add_argument(
        'username', help='Set a username to login to the mailserver.\n\rPassword will be asked on execute,')
    parser.add_argument(
        'subject', help='The Subject of your email, put the string in quotes.')
    parser.add_argument(
        'text_email', help='Type out your email but only text, put the message in quotes.')
    parser.add_argument(
        'html_email', help='Craft an email using html, put the string in quotes.')
    parser.add_argument(
        '-s', '--ssl', action='store_true', help='Use encryption to the mailserver.')

    subparsers = parser.add_subparsers(help='commands', dest='commands')

    single_mailer = subparsers.add_parser('spear_fish', help='Send email to a single recipient.')
    single_mailer.add_argument('your_email', help='The email address you will be sending to, the recipient.')

    mass_mailer = subparsers.add_parser('mass_mailer', help='Send an email to a list of emails.')
    mass_mailer.add_argument('your_email', help='A file with email addresses you will be sending to, the recipients.\n\rA new email address on each line of the file.')

    args = parser.parse_args()
    return args


def main():
    """Request password and ompile emailm then send."""
    args = parse_arguments()
    print args

    password = getpass.getpass()

    email_content = Email(args.my_email, args.your_email,
                          args.subject, args.text_email, args.html_email)
    send_email = SendEmail(args.username, password, args.mailserver,
                           args.my_email, args.your_email, args.ssl, email_content.compile_email)
    send_email.connect_send_disconnect()


if __name__ == '__main__':
    main()
