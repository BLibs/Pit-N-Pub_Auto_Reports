# SpotOn Subscription Report Automation

This script automates the downloading, parsing, and forwarding of SpotOn subscription reports received via Gmail. The script is designed to save ink and paper by eliminating the printing of the email body and only printing the PDF attachments.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)

## Introduction

SpotOn subscriptions are sent to Gmail accounts, which receive daily reports. The sites use HP ePrint to print these reports directly. However, this method forces the printing of the email body, which includes a large SpotOn image, consuming a lot of ink and paper.

This script downloads the attachments, extracts the PDF files, and forwards them to the printer without the email body. The script is hosted and scheduled to run every morning on the server at Northside. Each site has its own printer address, intermediary email account, and script.

## Features

- Deletes old files from the previous day to prevent reprinting
- Downloads all unread report files from the reporting email inbox
- Forwards PDF attachments to the printer without the email body

## Installation

1. Clone the repository:
    ```sh
    git clone https://https://github.com/BLibs/Pit-N-Pub_Auto_Reports.git
    ```
2. Navigate to the project directory:
    ```sh
    cd Pit-N-Pub_Auto_Reports
    ```
3. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

## Configuration

Create a `config.py` file in the project directory and define the following variables:

```python
PATH = 'path_to_save_files'
HOST = 'your_imap_host'
EMAIL = 'your_email'
PASSWORD = 'your_email_password'
RECIPIENT_EMAIL = 'printer_email_address'
SMTP_SERVER = 'your_smtp_server'
SMTP_PORT = your_smtp_port
```

## Usage 

The script can either be ran directly as a Python file or compiled into an .exe with Pyinstaller
1. Run the script to start the automation process:
    ```sh
    python main.py
    ```
2. Compile the .exe which can then be ran in any environment, in my case as a scheduled task in Windows.
