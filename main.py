from config import *
from email.message import EmailMessage
from imbox import Imbox
import os
import shutil
import smtplib
import time
import traceback

'''SpotOn Subscriptions are sent to Gmail accounts that I set up to get the reports every day. The sites are using HP 
   eprint, which would receive the subscription emails directly and print them, but forces the printing of the body of 
   the email. The body would be a large SpotOn image, using a ton of ink and a full sheet of paper per report. The Gmail 
   accounts receive the reports, and then we download the attachments, parse out the pdf files, and forward them to the 
   printer with no body, saving ink and paper. This script is hosted and scheduled to run every morning on the server at 
   Northside. Each site has their own printer address, middle-man email account, and script.'''


# Function for deleting old files from previous day on each pass, so they do not print again
def delete_old_files():
    folder = PATH
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))


# Function for downloading all unread report files from the reporting email inbox
def get_new_reports():
    if not os.path.isdir(PATH):
        os.makedirs(PATH, exist_ok=True)

    mail = Imbox(HOST, username=EMAIL, password=PASSWORD, ssl=True, ssl_context=None, starttls=False)
    messages = mail.messages(unread=True)  # Getting only the messages that are unread

    for (uid, message) in messages:
        mail.mark_seen(uid)  # Mark message as read

        for idx, attachment in enumerate(message.attachments):
            try:
                att_fn = attachment.get('filename')
                if att_fn[-4:] == ".pdf":  # Checking to see if this is a pdf file
                    download_path = f"{PATH}/{att_fn}"
                    print(download_path)
                    with open(download_path, "wb") as fp:
                        fp.write(attachment.get('content').read())
            except:
                print(traceback.print_exc())

    mail.logout()


# Function for attaching the pdf files and sending the email to the printer. Takes the subject as a param
def send_email(subject):
    msg = EmailMessage()
    msg.set_content("")  # Email does not need a body. This would print out on its own sheet of paper
    msg['Subject'] = subject
    msg['From'] = EMAIL
    msg['To'] = RECIPIENT_EMAIL

    for file in os.listdir(PATH):
        attachment = os.path.join(PATH, file)

        with open(attachment, 'rb') as file:
            file_data = file.read()
            file_name = file.name
            msg.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=file_name)

    # Send the email
    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
        server.starttls()  # Secure the connection
        server.login(EMAIL, PASSWORD)
        server.send_message(msg)

    print("Email sent successfully!")
    time.sleep(5)


if __name__ == '__main__':

    '''MAIN APPLICATION LOGIC'''
    # Remove all files from the local directory. Dir would be holding yesterdays' files on each pass
    delete_old_files()

    # Download the new report files
    get_new_reports()

    # Attach all files to an email and send to the printer
    send_email("SpotOn Reports")
