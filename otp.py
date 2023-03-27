import random
import pywhatkit

def sendOTP():
    number=random.randint(0,9999)
    pywhatkit.sendwhatmsg_instantly("+91 9987380617",message=str(number),wait_time=10)
    user_num=0
    while(user_num!=number):
        try:
            user_num=int(input("Enter OTP:"))
            if(user_num==number):
                print("Registration Successful!")
                break
            else:
                print("Incorrect OTP")
        except ValueError:
            print("PLEASE ENTER NUMBERS ONLY")

sendOTP()
