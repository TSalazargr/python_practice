import datetime

day = int(input("Day: ")) # Get all input as numbers
month = int(input("Month: "))
year = int(input("Year: "))

date = datetime.date(year, month, day)

print(date)
