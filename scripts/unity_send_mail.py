#!/usr/bin/env python
"""

"""

import argparse
import getpass

from mailer.mail_utilities import Email
from mailer.mail_utilities import SendEmail


def parse_args():
    """"""
    legal_statement = '[*] unity_send_mail Copyright (C) 2018 Mitch O\'Donnell\n    This program comes with ABSOLUTELY NO WARRANTY.\n    This is free software, and you are welcome to redistribute it\nunder certain conditions.'
    url = '[*] https://github.com/BuildAndDestroy/Unity'
    epilog = '{}\n\n{}'.format(url, legal_statement)
    parser = argparse.ArgumentParser(description=__doc__, epilog=epilog, formatter_class=argparse.RawTextHelpFormatter)

    subparsers = parser.add_subparsers(help='commands', dest='commands')

    single_mailer = subparsers.add_parser('spear_fish', help='Send a single email.')
    single_mailer.add_argument('my_email', help='The email address you will be sending from as yourself.')
    single_mailer.add_argument('your_email', help='The email address you will be sending to, the recipient.')
    single_mailer.add_argument('mailserver', help='The mailserver we will connect to to send our email.')
    single_mailer.add_argument('subject', help='The Subject of your email, put the string in quotes.')
    single_mailer.add_argument('text_email', help='Type out your email but only text, put the message in quotes.')
    single_mailer.add_argument('html_email', help='Craft an email using html, put the string in quotes.')

    single_mailer.add_argument('-u', '--username', action='store_true', help='Set a username to login to the mailserver.')
    single_mailer.add_argument('-p', '--password', action='store_true', help='Set the password to login to the mailserver.')
    single_mailer.add_argument('-s', '--ssl', action='store_true', help='User encryption to the mailserver.')

    mass_mailler = subparsers.add_parser('mass_mailler', help='Send an email to a list of emails.')
    mass_mailler.add_argument('my_email', help='The email address you will be sending from as yourself.')
    mass_mailler.add_argument('your_email', help='A file with email addresses you will be sending to, the recipients.\n\rA new email address on each line of the file.')
    mass_mailler.add_argument('mailserver', help='The mailserver we will connect to to send our email.')
    mass_mailler.add_argument('subject', help='The Subject of your email, put the string in quotes.')
    mass_mailler.add_argument('text_email', help='Type out your email but only text, put the message in quotes.')
    mass_mailler.add_argument('html_email', help='Craft an email using html, put the string in quotes.')

    mass_mailler.add_argument('-u', '--username', action='store_true', help='Set a username to login to the mailserver.')
    mass_mailler.add_argument('-p', '--password', action='store_true', help='Set the password to login to the mailserver.')
    mass_mailler.add_argument('-s', '--ssl', action='store_true', help='User encryption to the mailserver.')

    args = parser.parse_args()
    return args

def main():
    """"""
    args = parse_args()
    

if __name__ == '__main__':
    main()