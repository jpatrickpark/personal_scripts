#!/home/jp/anaconda3/bin/python
import sendgrid
import os
from sendgrid.helpers.mail import *
import argparse
import sys

my_email_address = 'qkrwjdrb@gmail.com'

def send_email_to_myself(title, content):
    send_email(my_email_address, title, content)

def send_email(addr, title, content):
    sg = sendgrid.SendGridAPIClient(apikey=os.environ.get('SENDGRID_API_KEY'))
    from_email = Email(addr)
    to_email = Email(addr)
    subject = title
    content = Content("text/plain", content)
    mail = Mail(from_email, subject, to_email, content)
    mail.add_category(Category("self"))
    response = sg.client.mail.send.post(request_body=mail.get())
    if response.status_code != 202:
        print('failure')

def get_args():
    parser = argparse.ArgumentParser(description = 'Send email to self.')
    parser.add_argument('title')
    parser.add_argument('content')
    return parser.parse_args()

if __name__ == '__main__':
    args = get_args()
    send_email_to_myself(args.title, args.content)
