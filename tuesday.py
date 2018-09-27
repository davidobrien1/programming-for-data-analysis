import datetime

today = datetime.datetime.today()
dayofweek = today.weekday()

print ("Let's check if it's Tuesday.")

if dayofweek == 1: # colon says here's what to do it this is true
    print("It's Tuesday!")
elif dayofweek == 0:
    print("It's not Tuesday.")
    print("Luckily, it will be Tuesday tomorrow!")
else:
    print("Unfortunately, it's not Tuesday.")

print("Thanks for checking if it's Tuesday.")