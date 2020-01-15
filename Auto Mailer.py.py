'''
Project         :       Auto Mailer
Author          :       Sanjay
Date            :       15/01/2020
'''
        
#!/usr/bin/python3
import os
import sys
import requests
import httplib2

#For using gmail api service
from googleapiclient import discovery 
from oauth2client.client import flow_from_clientsecrets
from oauth2client.file import Storage
from googleapiclient.discovery import build
from oauth2client import client, tools

#For encoding binary data and turning it into text so
#that it's more easily transmitted in things like e-mail and HTML form data.
import base64

#For E-mail formatting
from email.message import Message
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


#====================================Auto Gmail===========================================
def get_credentials():
	"""Gets valid user credentials from storage.

	If nothing has been stored, or if the stored credentials are invalid,
	the OAuth2 flow is completed to obtain the new credentials.

	Returns:
	Credentials	-	the obtained credential.
	"""

	# Api endpoint for sending emails
	SCOPES = 'https://www.googleapis.com/auth/gmail.send'

	CLIENT_SECRET_FILE = 'Gmail_credentials\client_secret.json'
	APPLICATION_NAME = 'Mail Automation'
	
	home_dir = os.path.expanduser('~')
	credential_dir = os.path.join(home_dir, 'Gmail_credentials\.credentials')
	if not os.path.exists(credential_dir):
		os.makedirs(credential_dir)
	credential_path = os.path.join(credential_dir, 'gmail_user_credential.json')
	print(credential_path)
	store = Storage(credential_path)
	credentials = store.get()
	
	if not credentials or credentials.invalid:
		try:
			flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
			flow.user_agent = APPLICATION_NAME
			flags = tools.argparser.parse_args(args=[])
			if flags:
				credentials = tools.run_flow(flow, store, flags)
		
		except Exception as error:
			print('\nAn error occurred while reading client secret file: %s' % error)
			sys.exit("Please download client_secret.json file from https://console.developers.google.com/apis/credentials before proceeding further")
		
	print('Storing credentials to ' + credential_path)
	return(credentials)


def get_gmail_service():
	"""	
	Get the service of gmail through Gmail api
	
	returns a object of gmail service which will be further used. 
	"""
	
	credentials = get_credentials()

	# Create an httplib2.Http object to handle our HTTP requests, and authorize it using credentials.authorize()
	http = httplib2.Http()

	# http is the authorized httplib2.Http() 
	http = credentials.authorize(http)        #or: http = credentials.authorize(httplib2.Http())
	
	gmail_service = discovery.build('gmail', 'v1', http=http) #create a gmail service object
	return(gmail_service)
	
	
def create_message():
        """Create a message for an email.

        Returns:
        An object containing a base64url encoded email object.
        """	

        To = "Recipient Email address goes here"
        To_cc = "CC Recipient Email address goes here"
        subject = "Subject Goes here"

        message = MIMEMultipart('mixed')


                
        message_html = """\
                <html>
                        <head>Hi,<br></head>
                        <body>
                                <p><b><u>This is HTML message</u></b><br><br></p>
                        </body>
                </html>
                """
        message.attach(MIMEText(message_html, 'html'))

        message_plain = "This is plain message."
        message.attach(MIMEText(message_plain, 'plain'))

        message['Subject'] = subject
        message['To'] = To
        message['Cc'] = To_cc

        raw_message = base64.urlsafe_b64encode(message.as_bytes())
        raw_message = raw_message.decode()
        body  = {'raw': raw_message}
        return(body)

def send_message():
	"""	
		Send message to the listed recipients
	"""
	
	mail_msg = create_message()
	gmail_service = get_gmail_service()
	
	try:	
		message = (gmail_service.users().messages().send(userId="me", body=mail_msg).execute())
		print('Message Lable: %s' %message['labelIds'][0])
		
	except Exception as error:
		print('Sending Message Failed:\n  An error occurred: %s' % error)

def main():
	send_message()

if __name__ == '__main__':
	main()
