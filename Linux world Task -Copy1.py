#!/usr/bin/env python
# coding: utf-8

# # Python project 

# In[ ]:


#pip install twilio


# # Send SMS Msg using python

# In[ ]:


from twilio.rest import Client

# Your Twilio account SID and Auth Token
account_sid = 'ACc8a6ea312b7ea7b9034b467bc3d200a0'
auth_token = '450021678b7335701e8f97c956190f6a'

client = Client(account_sid, auth_token)

# Send SMS to yourself
message = client.messages.create(
    body="hii anshu",
    from_='+12532377764',  # my Twilio phone number
    to='+917061901464'     # my own phone number
)

print(f"Message sent with SID: {message.sid}")


# # Send Email using python 

# In[ ]:


import smtplib

email = input("SENDER EMAIL: ")  
receiver_email = input("RECEIVER EMAIL: ")
subject = input("SUBJECT: ")
message = input("MESSAGE: ")

text = f"Subject: {subject}\n\n{message}"

server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()

# Consider using environment variables for the password for security
server.login(email, "vzhh qzjw kdbz qzfg")  #my server login password

server.sendmail(email, receiver_email, text)
print(f"Email has been sent to {receiver_email}")  

server.quit()  


# ## Scrap top5 search results from google using the python code

# In[ ]:


#pip install google-search-results


# In[ ]:


from serpapi import GoogleSearch

# Your API key from SerpApi
api_key = "16d3d75fac27426d539d3887705777a6b4725e3936fd111d979941ecd91368ee"

query = input("Enter the search query: ")

params = {
    "engine": "google",
    "q": query,
    "num": "5",
    "api_key": api_key
}

search = GoogleSearch(params)
results = search.get_dict()

# Extract and print the top 5 results
top_results = results.get("organic_results", [])

for i, result in enumerate(top_results, start=1):
    print(f"Result {i}:")
    print(f"Title: {result['title']}")
    print(f"Link: {result['link']}")
    print(f"Snippet: {result.get('snippet', 'No description available')}")
    print("-" * 40)


# ## Find the current geo coordinates and location using the Python code 

# In[ ]:


#pip install geocoder


# In[ ]:


import geocoder

# Get the current location of the IP address
g = geocoder.ip('me')

# Extract the latitude and longitude
lat, lng = g.latlng

print(f"Latitude: {lat}, Longitude: {lng}")

# Get the address or location name
location = g.address

print(f"Location: {location}")


# ## Convert text-to-audio using the python code

# In[ ]:


#pip install gtts


# In[ ]:


from gtts import gTTS
import os

# The text you want to convert to audio
text = "Hii i am Google assistance."

# Convert the text to speech using gTTS
tts = gTTS(text=text, lang='en')  # 'en' for English language

# Save the audio to a file
tts.save("output.mp3")

# Play the audio file
os.system("start output.mp3")  # For Windows
# os.system("mpg321 output.mp3")  # For Linux


# ## Control volume of you laptop using python.

# In[ ]:


#!pip install --upgrade pycaw


# In[ ]:


from pycaw.pycaw import AudioUtilities, ISimpleAudioVolume
import ctypes

CLSCTX_ALL = 23  # 23 is the combined value of CLSCTX_INPROC_SERVER | CLSCTX_LOCAL_SERVER | CLSCTX_REMOTE_SERVER

# Get the default audio device
devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(
    ISimpleAudioVolume._iid_, 
    CLSCTX_ALL,  # Use the correct COM activation context
    None
)
volume = interface.QueryInterface(ISimpleAudioVolume)

# Function to set volume
def set_volume(level):
    # level should be between 0.0 and 1.0
    if 0.0 <= level <= 1.0:
        volume.SetMasterVolume(level, None)
        print(f"Volume set to {level * 100}%")
    else:
        print("Volume level must be between 0.0 and 1.0")

# Example usage
set_volume(0.5)  # Set volume to 50%


# ## Connect to your mobile and send sms from your mobile messaging app using python.

# In[ ]:


from twilio.rest import Client

# Your Twilio account SID and Auth Token
account_sid = 'AC8e66ceec1e40b20104914ad5f00a348d'
auth_token = '6021f070c92a5d05acc82a7d550fdf65'

client = Client(account_sid, auth_token)

# Send SMS to yourself
message = client.messages.create(
    body="hii anshu",
    from_='+16315934383',  # Your Twilio phone number
    to='+917485822447'     # Your own phone number
)

print(f"Message sent with SID: {message.sid}")


# ## Create a function to Send bulk email using python.

# In[ ]:


import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_bulk_emails(smtp_server, port, username, password, subject, body, recipients):
    """
    Sends bulk emails.

    Parameters:
    smtp_server (str): The SMTP server address.
    port (int): The port number for the SMTP server.
    username (str): The username for the SMTP server.
    password (str): The password for the SMTP server.
    subject (str): The subject of the email.
    body (str): The body of the email.
    recipients (list): A list of recipient email addresses.

    Returns:
    None
    """
    # Create the email server connection
    server = smtplib.SMTP(smtp_server, port)
    server.starttls()  
    server.login(username, password)

    for recipient in recipients:
        msg = MIMEMultipart()
        msg['From'] = username
        msg['To'] = recipient
        msg['Subject'] = subject

        msg.attach(MIMEText(body, 'plain'))

        try:
            server.sendmail(username, recipient, msg.as_string())
            print(f'Email sent to {recipient}')
        except Exception as e:
            print(f'Failed to send email to {recipient}. Error: {e}')

    server.quit()

smtp_server = 'smtp.example.com'
port = 587
username = 'your-email@example.com'
password = 'your-email-password'
subject = 'Test Bulk Email'
body = 'This is a test bulk email.'
recipients = ['recipient1@example.com', 'recipient2@example.com']

send_bulk_emails(smtp_server, port, username, password, subject, body, recipients)


# In[ ]:




