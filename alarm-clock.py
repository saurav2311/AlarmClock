# Kumar Saurav: saurav@qti.qualcomm.com 

# Alarm Clock & Countdown Clock and Timer

# This project is an alarm clock that allows the user to enter how long
# they would like to sleep for. The script will then do the math and
# wake users up by randomly selected a song to play.

import random, webbrowser, datetime, time
from datetime import datetime, timedelta

url1 = "https://www.youtube.com/watch?v=BIKarAqOB9I"                                                 #Enter your preferred URL here!
url2 = "https://www.youtube.com/watch?v=W_9KR3mYkUo&list=PL9Z_KwF-qaztJlEdtO1Kiw-6UKVZbk75I"
url3 = "https://www.youtube.com/watch?v=Uiv9btIuQnk&list=PL9Z_KwF-qaztJlEdtO1Kiw-6UKVZbk75I&index=3"
url4 = "https://www.youtube.com/watch?v=3fsJIhbA4Ik&list=PL9Z_KwF-qaztJlEdtO1Kiw-6UKVZbk75I&index=9"

Time = time.strftime("%H:%M:%S")

print("")
print ("Currently it is:", Time)
minutes_of_sleep = int(input("Enter the number of minutes you would like to sleep for:"))
hours_of_sleep = int(input("Enter the number of hours you would like to sleep for:"))
print("")

Alarm = (datetime.now() + timedelta(hours=hours_of_sleep) + timedelta(minutes=minutes_of_sleep)).strftime('%H:%M:%S')
print("You will be woken up at:", Alarm)
yes_no = str(input("Would you like to set this alarm? [Y/N]")).lower()
print("")

while yes_no == "y" or yes_no == "yes":

    while Time != Alarm:
        print("It is currently:", time.strftime("%H:%M:%S"))
        Time = time.strftime("%H:%M:%S")
        time.sleep(1)
        if Time == Alarm:
            print("")
            print("Time to wake up!")
            url = random.choice([url1, url2, url3, url4])
            webbrowser.open(url)
            break

# End. User can enter his/her preferred video urls for alarm!
