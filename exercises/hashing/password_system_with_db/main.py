import mysql.connector, random

my_db = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword",
  database="my_db"
)

if my_db.is_connected():
    print("Connection Successfully")

my_cursor = my_db.cursor()

def menu():
  while True:
    choice = input("Would you like to: \n 1 Sign up \n 2 log in \n 3 exit \n 1/2/3: ").strip()
    if choice == "1":
        sign_up()
        break
    elif choice == "2":
        log_in()
        break
    elif choice == "3":
        exit()
    else:
        print("Invalid value. Please input 1, 2 or 3.")
        continue

def sign_up():
    input_user():
    input_password():

def log_in():
    print("Log in")

def input_user():
    while True:
        inputed_user = input("Input your username: ").strip()
        if len(inputed_user) > 255:
            print("Your username is too long. Try another username that has less than 256 characters.")
            continue
        if check_username_exists(inputed_user) == True: # If username already in database
            print("This username is already taken. Try again.")
            continue
        break

def check_username_exists(inputed_user):
    sql = "SELECT EXISTS(SELECT 1 FROM user_password WHERE user = %s)"  # Check if user exists

    my_cursor.execute(sql, (inputed_user,))
    result = my_cursor.fetchone()[0]

    if result == 1:
        exists = True  # User exists
    else:
        exists = False  # User doesn't exist

    return exists

while True:
    menu()
