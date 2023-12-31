import random, mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword"
)

my_cursor = mydb.cursor()



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
    input_user()
    input_password()
    save_user_password_salt(inputed_user, hashed_password, salt)

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

def input_password():
    while True:
        inputed_password = input("Input your password: ").strip()

        if not (8 <= len(inputed_password) <= 20): # Checks if password is between 8 and 20 characters
            print("Invalid length. Your password should have between 8 and 20 characters. Try again.")
        else:
            break

    salt = random.randint(1000, 9999999)
    hashed_password = hash(f"{inputed_password}{salt}")

def save_user_password_salt(inputed_user, hashed_password, salt):
    sql = "INSERT INTO user_password (user, hash_salted_password, salt) VALUES (%s, %s, %s)"
    val = [inputed_user, hashed_password, salt]
    my_cursor.execute(sql, val)

while True:
    menu()
