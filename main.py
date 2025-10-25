#step1 :- Install required libraries
from twilio.rest import Client
from datetime import datetime, timedelta
import time
import os
from dotenv import load_dotenv

# Load secrets from .env file
load_dotenv()

#step2 :- Twilio credentials (loaded from .env)
account_sid = os.getenv("TWILIO_SID")
auth_token = os.getenv("TWILIO_AUTH")

Client = Client(account_sid, auth_token)



#step3 
def send_whatsapp_message(recipient_number, message_body):
    try:
        message = Client.messages.create(
            from_='whatsapp:+14155238886',
            to=f'whatsapp:{recipient_number}',
            body=message_body
        )

        print(f'Message sent successfully! Message SID: {message.sid}')

    except Exception as e:
        print('An error occurred:', e)


#step4 :- user input
name = input('Enter the recipient name = ')
recipient_number = input('Enter the recipient Whatsapp number with coutry code : ')
message_body = input(f'enter the message you want to send to {name}: ')

#step5 :- parse date time and calculate delay
date_str = input('enter the date to send the message (YYYY-MM-DD): ')
time_str = input('enter the time to send the message (HH-MM in 24hour format): ')

#datetime
schedule_datetime = datetime.strptime(f'{date_str} {time_str}', "%Y-%m-%d %H:%M")
current_datetime = datetime.now()

#calculate delay
time_difference = schedule_datetime - current_datetime
delay_seconds = time_difference.total_seconds()


if delay_seconds<=0:
    print('The specified time is in the past . Please enter a future date and time: ')
else:
    print(f'Message scheduled to be sent to {name} at {schedule_datetime}.')

#wait until the scheduled time
time.sleep(delay_seconds)

#send the message
send_whatsapp_message(recipient_number,message_body)