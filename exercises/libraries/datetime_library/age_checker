import datetime

def age_checker():
    today = datetime.datetime.now().date()
    birthdate = create_date()
    difference_in_years = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))

    if difference_in_years >= 18:
        print("You're not a minor.")
        minor = False
    else:
        print("You're under 18.")
        minor = True

    return minor
    
def create_date():
    today = datetime.datetime.today()
    present_year = datetime.datetime.today().year  # Extract today's year

    while True:
        try:
            birthyear = int(input("What year were you born?: "))
        except:
            print("Invalid value. Input must be a number. Try again.")
            continue

        if not (1900 <= birthyear <= present_year):
            print(f"Invalid value. The value must be between 1900 and {present_year}.")
        else:
            break

    while True:
        try:
            birthmonth = int(input("What month were you born? (Input the month as a number): "))
        except:
            print("Invalid value. Input must be a number. Try again.")
            continue

        if birthmonth <= 0 or birthmonth > 12:
            print(f"Invalid value. The value must be between 1 and 12.")
        else:
            break

    while True:
        try:
            birthday = int(input("What day were you born?: "))
        except:
            print("Invalid value. Input must be a number. Try again.")
            continue

        try:
            birthdate = datetime.date(year=birthyear, month=birthmonth, day=birthday)
            break
        except:
            print("Invalid value. The day inputed is not possible. Try again.")

    return birthdate

age_checker()

###########################

today.year - birthdate.year: This calculates the difference in years between the current year (today.year) and the birth year (birthdate.year). This part alone would give you the difference in years if you only considered the year component.

((today.month, today.day) < (birthdate.month, birthdate.day)): This is a comparison between tuples (today.month, today.day) and (birthdate.month, birthdate.day). It's using the fact that in Python, when you compare tuples, it compares element-wise, starting from the first element. If the first elements are equal, it moves to the next elements until a difference is found or all elements are compared.

(today.month, today.day): Creates a tuple of the current month and day.
(birthdate.month, birthdate.day): Creates a tuple of the birth month and day.
This comparison returns True if the tuple representing the current month and day is less than the tuple representing the birth month and day. Essentially, it checks if the current date (ignoring the year) is earlier than the birthdate (ignoring the year).

- ((today.month, today.day) < (birthdate.month, birthdate.day)): This part subtracts 1 from the year difference (today.year - birthdate.year) if the birthdate (month, day) tuple is greater than the current date's (month, day) tuple. This is a way to account for cases where the birthdate hasn't occurred yet in the current year.

The entire expression combines these components to accurately calculate the age in years, adjusting for whether the birthday has already occurred in the current year.
