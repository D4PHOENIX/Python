import time

timeNow = time.strftime("%H")

if timeNow < "12" and timeNow > "4":
    print("Good Morning")
elif timeNow < "18" and timeNow > "12":
    print("Good Afternoon")
elif timeNow < "21" and timeNow > "18":
    print("Good Evening")
elif timeNow < "24" and timeNow > "21":
    print("Good Night")
else:
    print("Go to sleep")
