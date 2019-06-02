#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
import tempfile
import subprocess
import smtplib
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import COMMASPACE, formatdate


name = "pico"
version = "0.1.0"


def send_mail(send_from, send_to, subject, text, file_attach,
        server="email-smtp.us-east-1.amazonaws.com"):
    assert isinstance(send_to, list)

    msg = MIMEMultipart()
    msg['From'] = send_from
    msg['To'] = COMMASPACE.join(send_to)
    msg['Date'] = formatdate(localtime=True)
    msg['Subject'] = subject

    msg.attach(MIMEText(text))

    with open(file_attach, "rb") as attach:
        part = MIMEApplication(
            attach.read(),
            Name="report.txt"
        )

    # After the file is closed
    part['Content-Disposition'] = 'attachment; filename="report.txt"'
    msg.attach(part)

    smtp = smtplib.SMTP(server, 587)
    smtp.starttls()
    smtp.login("Smtp Username", "Smtp Password")
    smtp.sendmail(send_from, send_to, msg.as_string())
    smtp.close()


def main(argv):
    # argv[2] holds the command to run and generate the attachment (report.txt)
    print("> Executing {0}".format(argv[2]))
    message_body = subprocess.Popen(argv[2].split(), stdout=subprocess.PIPE).stdout.read()
    tmp = tempfile.NamedTemporaryFile("w")
    tmp.write(message_body)
    tmp.flush()
    print("> Temporary message created at: {0}".format(tmp.name))
    print("> Sending mail message")
    send_mail(
        "Name From <from@example.com>",
        ["toA@example.com", "toB@example.com", "toC@example.com"],
        "Subject",
        "Message body",
        tmp.name,
    )


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt as e:
        sys.exit(0)
