# Auto_Mailer
Send mail automatically using gmail Api.

Using google api for mail sending

    1. You need a google account - either google apps or gmail. So, if you haven't got one, go get one.
    2. Get yourself to the developers console --> https://console.developers.google.com
    3. Create a new project, and wait 4 or 400 seconds for that to complete.
    4. Navigate to https://console.developers.google.com/apis/credentials
    5. Under OAuth Client ID, select Create New Client ID
    6. Choose Application type as Other and Create.
    You should now have a button Download JSON. Do that. It's your client_secret.json—the passwords so to speak

Before Creating New Client ID, Performs these steps:
You have to give your application a "Product Name" to avoid some odd errors. (see how much I suffered to give you this ;-)

    Navigate to API's & auth -> Consent Screen
    Choose your email
    Enter a PRODUCT NAME. It doesn't matter what it is. "Foobar" will do fine.
    Save
	
Newsflash! Whoa. Now there's even more!
	Navigate to API's & auth -> APIs -> Gmail API
    Click the button Enable API. 

Google API scopes:
	1. https://www.googleapis.com/auth/gmail.send	Send messages only. No read or modify privileges on mailbox.
	2. https://www.googleapis.com/auth/gmail.compose	Create, read, update, and delete drafts. Send messages and drafts.
  
  
To install required python packages:  
>>> pip install -r requirements.txt
  
To Install googleapiclient Packages:
>>> pip install --upgrade google-api-python-client

<b>Usage</b>
I developed this piece of code for sending emails to the developers about the bugs reported on the project. This was a part of program which get the list of bugs created and assigned to the developers from the Project management tool, create ticktes on jira for them and then send emails to the developers on daily basis.
