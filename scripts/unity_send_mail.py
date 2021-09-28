#!/usr/bin/env python3
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


def parse_args() -> tuple:
    """Accept user input, also create the help menu."""
    legal_statement = '[*] unity_send_mail Copyright (C) 2018 Mitch O\'Donnell\n    This program comes with ABSOLUTELY NO WARRANTY.\n    This is free software, and you are welcome to redistribute it\nunder certain conditions.'
    url = '[*] https://github.com/BuildAndDestroy/Unity'
    epilog = '{}\n\n{}'.format(url, legal_statement)
    parser = argparse.ArgumentParser(
        epilog=epilog, formatter_class=argparse.RawTextHelpFormatter)

    subparsers = parser.add_subparsers(help='commands', dest='commands')

    single_mailer = subparsers.add_parser(
        'spear_fish', help='Send emails.')
    single_mailer.add_argument(
        'my_email', help='The email address you will be sending from as yourself.')
    single_mailer.add_argument('my_display_name', help='My display name that I want displayed in the email')
    single_mailer.add_argument(
        'your_email', help='The email address, or file full of email addresses, you will be sending to. The recipient.')
    single_mailer.add_argument(
        'mailserver', help='The mailserver we will connect to to send our email.')
    single_mailer.add_argument(
        'username', help='Set a username to login to the mailserver. Password will be asked on execute.')
    single_mailer.add_argument(
        'subject', help='The Subject of your email, put the string in quotes.')
    single_mailer.add_argument(
        'html_email', help='Full path to your html email.')

    single_mailer.add_argument(
        '-s', '--ssl', action='store_true', help='Use encryption to the mailserver.')

    args = parser.parse_args()
    return args


def main() -> None:
    """Request password and ompile emailm then send."""
    args = parse_args()
    print(args)

    password = getpass.getpass()
    if args.commands == 'spear_fish':
       #email_content = Email(args.my_email, args.my_display_name, args.your_email,
       #                      args.subject, args.html_email)
       #send_email = SendEmail(args.username, password, args.mailserver,
       #                       args.my_email, args.my_display_name, args.your_email, args.ssl, email_content.compile_email)
       #send_email.connect_send_disconnect()
       send_email = SendEmail(args.my_email, args.my_display_name, args.your_email, args.subject, args.html_email, args.username, password, args.mailserver, args.ssl)
       send_email.connect_send_disconnect()
    else:
        print('[*] Use a positional argument!')

if __name__ == '__main__':
    main()
