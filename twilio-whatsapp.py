#!/usr/bin/python3.4

from twilio.rest import Client

import schedule
import time
from datetime import datetime

account_sid = '<your sid>'
auth_token = '<your auth token>'
client = Client(account_sid, auth_token)

birthdayList =(
    (21,9,"Nakul"),
    (22,4,"Jinni"),
    (22,5,"Frank"),
    (23,7,"Rubi")
)

# for check
def chkIfBirthday():
    currentDay = datetime.now().day
    currentMonth = datetime.now().month

    for (day, month, name) in birthdayList:
        if day == currentDay and month == currentMonth:
            sendWhatsapp("today is "+name+"'s birthday")


# for whatsapp
def sendWhatsapp(message):
    message = client.messages.create(
        from_='whatsapp:<assigned twilio number>',
        body='Today is '+message,
        to='whatsapp:<your whatsapp number>'
    )
    print(message.sid)


# shedular
schedule.every().day.do( chkIfBirthday )
while True:
    schedule.run_pending()
    time.sleep(1)
