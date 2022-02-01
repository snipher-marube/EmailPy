import smtplib
from email.message import EmailMessage
import json
import imghdr
import os

#open your jason file with multiple email addresses
contacts = json.loads(open('emails.json'))


#if you exported your  email address and password to your machine variables access then as below
#Highly recommended way is export your secret keys the get then as below
email_address = os.environ.get('email')
password = os.environ.get('password')

#if not exported hardcode the here as bellow
EMAIL_ADDRESS = 'Your app email'
EMAIL_PASSWORD = 'Your app password'

msg = EmailMessage()
msg['Subject'] = 'Your Subject title'
msg['From'] = EMAIL_ADDRESS
msg['To'] = contacts
msg.set_content('This is your content area')

#add html file type
msg.add_alternative("""\
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport"
          content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Snipher</title>
</head>
<body>
    <h1 style="color:red;">This is HTML Email</h1>

</body>
</html>
""", subtype='html')

#list the files to attach
files = ['admin.jpg']

for file in files:
    #open the file to read
    with open(file, 'rb') as f:
        file_data = f.read()

        #determine file type e.g jpeg, png
        file_type = imghdr.what(f.name)
        file_name = f.name

    #attach the file
    msg.add_attachment(file_data, maintype='image', subtype=file_type, filename=file_name)

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    smtp.send_message(msg)


