# SpotOn Subscription Report Automation

This Python script automates the process of handling SpotOn subscription reports sent to Gmail accounts. The script downloads the PDF attachments from the emails, removes the email body to save ink and paper, and then forwards the attachments to the specified printer. This script is scheduled to run every morning on the server at Northside.

## Features

- Deletes old files from the previous day to prevent re-printing.
- Downloads unread report files from the Gmail inbox.
- Sends the downloaded PDF files to the printer without the email body.

## Requirements

- Python 3.x
- `imbox` library for interacting with the email inbox
- `smtplib` for sending emails
- `email` library for creating email messages

## Configuration

Ensure you have a `config.py` file with the following variables set:

```python
# config.py
PATH = 'path/to/your/local/directory'
HOST = 'imap.gmail.com'
EMAIL = 'your.email@gmail.com'
PASSWORD = 'yourpassword'
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587
RECIPIENT_EMAIL = 'printer.email@domain.com'
