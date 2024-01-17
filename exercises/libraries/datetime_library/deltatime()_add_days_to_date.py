import datetime

today = datetime.date.today() # Today's date

print(today)

difference = datetime.timedelta(days=14) # The difference I want
new_date = today + difference # Add today to the delta difference to see the date in 14 days time.

print(new_date) 

one_week_later = datetime.timedelta(weeks=1)
new_date = new_date + one_week_later

print(new_date)

# Note: 'months' is not a valid argument inside timedelta(), as months have different lengths

# Syntax : datetime.timedelta(days=0, seconds=0, microseconds=0, milliseconds=0, minutes=0, hours=0, weeks=0) 
