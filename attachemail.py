#!/usr/bin/env python3

import os
import re
import sys
import smtplib

from getpass import getpass
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

SMTP_SERVER = 'smtp.gmail.com' # gmail smtp server
SMTP_PORT = 587 # gmail smtp port

def send_email(sender, recipient):
    """ sends email message """
    msg = MIMEMultipart()
    msg['To'] = recipient
    msg['From'] = sender
    subject = input('Enter your email subject: ')
    msg['subject'] = subject
    message = input('Enter your input here: ')
    part = MIMEText('text', "plain")
    part.set_payload(message)
    msg.attach(part) # attach body message

    # attach an image in the current director
    fileloc = input('Please Enter in the location you want to retrieve the file: ')     # file location
    filename = input('Please enter file name u want to attach: ')       # filename
    path = os.path.join(fileloc, filename)      # us os.path.join to the path together, this helps us display what we want to attach
    if os.path.exists(path):
        img = MIMEImage(open(path, 'rb').read(), _subtype="jpg") """ type of f
        ile, to make it more flexible change the _subtype= to a value that the user can enter """
        img.add_header('Content-Disposition', 'attachment', filename = filename) # attach image as a header
        msg.attach(img) # attaching image to email

    # create smtp session
    session = smtplib.SMTP(SMTP_SERVER, SMTP_PORT) # Must always have a server client established
    session.ehlo()
    session.starttls()
    session.ehlo
    password = getpass('Enter password: ')
    session.login(sender, password) # login session, must configure google work

    # sendmail
    session.sendmail(sender, recipient, msg.as_string())
    print("You sent email to {0}.".format(recipient))
    session.quit()

if __name__ == '__main__':
    sender = input("Enter the sender email addres: ")
    recipient = input("Enter the sender email address: ")
    send_email(sender, recipient)
