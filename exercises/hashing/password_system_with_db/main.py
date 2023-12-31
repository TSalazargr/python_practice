import random, mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword"
  database="mydatabase"
)

my_cursor = mydb.cursor()

if my_db.is_connected():
    print("Connection Successfully")

my_cursor.execute("CREATE TABLE IF NOT EXISTS user_password (id INT AUTO_INCREMENT PRIMARY KEY, user VARCHAR(255), hash_salted_password VARCHAR(255), salt VARCHAR(255))")

print("Table 'user_password' created successfully.")

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
    print("Sign up")
    input_user()
    input_password()
    save_user_password_salt(inputed_user, hashed_password, salt)

def log_in():
    print("Log in")
    while True:
        inputed_user = input("Input your username: ").strip()

        if check_username_exists(inputed_user) = False:
            print("Username not found. Try again.")
            continue
        else:
            salt, hash_salted_password = extract_password(inputed_user)

        attempt = 0

        while attempt < 3:

            inputed_password = input("Input your password: ")
            inputed_password = f"{inputed_password}{salt}"
            inputed_password = hash(inputed_password)

            if inputed_password == hash_salted_password:
                print("Access granted")
                break
            else:
                attempt += 1
                print("Wrong password. Try again.")

        if attempt == 3:
            print("Too many failed attempts. Access denied.")

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

def extract_password(inputed_user):
    sql = "SELECT salt, hash_salted_password FROM user_password WHERE user = %s"
    val = inputed_user
    my_cursor.execute(sql, val)
    my_result = my_cursor.fetchall()

    if my_result:  # If data is found
        salt, hash_salted_password = my_result[0]  # Extract salt and hashed password from the first row found
        return salt, hash_salted_password
    else:
        return None, None  # Or handle the case where no data is found

while True:
    menu()
