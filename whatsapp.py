import pywhatkit
from datetime import timedelta
import datetime
msg=["Hello","Kidhar","H","Bhai","?"]
for i in msg:
    now=datetime.datetime.now()+timedelta(minutes=1)
    hour=now.strftime("%H")
    minute=now.strftime("%M")
# syntax: phone number with country code, message, hour and minutes
    m=str(i)
    pywhatkit.sendwhatmsg_instantly("+91 9321534299",message=m,wait_time=15)


