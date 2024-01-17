import datetime

event = input("Input the event: ").capitalize()

year = int(input("Input the year: "))
month = int(input("Input the month: "))
day = int(input("Input the day: "))

event_date = datetime.date(year, month, day)

today = datetime.date.today()

difference = event_date - today
difference = difference.days # Converts difference into days

if difference == 0:
  print(f"Today is {event}!")
elif difference > 0:
  print(f"{difference} days left for the event!")
elif difference < 0:
  print(f"{event} was {-difference} days ago.")
