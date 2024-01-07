import mysql.connector

my_db = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword",
  database="my_db"
)

my_cursor = mydb.cursor()

if mydb.is_connected():
    print("Connection Successfully")

my_cursor.execute("CREATE TABLE IF NOT EXISTS user_password (id INT AUTO_INCREMENT PRIMARY KEY, user VARCHAR(255), hash_salted_password VARCHAR(255), salt VARCHAR(255))")

print("Table 'user_password' created successfully.")

def menu():
  access = False
  while True:
    choice = input("Would you like to: \n 1 Sign up \n 2 log in \n 3 exit \n 1/2/3: ").strip()
    if choice == "1":
        sign_up()
        break
    elif choice == "2":
        access = log_in()
        print(f"Login successful: {access}")
        break
    elif choice == "3":
        exit()
    else:
        print("Invalid value. Please input 1, 2 or 3.")
  return access


def sign_up():
    print("Sign up")
    inputed_user = input_user()
    inputed_password, hashed_password, salt = input_password()
    save_user_password_salt(inputed_user, hashed_password, salt)

def log_in():
    print("Log in")
    while True:
        inputed_user = input("Input your username: ").strip()

        if check_username_exists(inputed_user) == False:
            print("Username not found. Try again.")
            continue
        else:
            salt, hash_salted_password = extract_password(inputed_user)
            break
    attempt = 0

    while attempt < 3:

        inputed_password = input("Input your password: ")
        inputed_password = f"{inputed_password}{str(salt)}" # Append the salt
        inputed_password = hashlib.sha256(inputed_password.encode()).hexdigest()

        if inputed_password == hash_salted_password: # Make sure both variables are strings
            access = True
            break
        else:
            attempt += 1
            print("Wrong password. Try again.")

        if attempt == 3:
            print("Too many failed attempts. Access denied.")
            exit()
    return access

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
    return inputed_user

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
    inputed_password = password_valid()
    salt = random.randint(1000, 9999999)
    hashed_password = hashlib.sha256(f"{inputed_password}{salt}".encode()).hexdigest()

    return inputed_password, hashed_password, salt

def password_valid():
    special_characters = "!¡¿?@,._-[]{}()=/$%'<>"
    found_special = False
    found_capitalized = False
    while True:
        inputed_password = input("Input your password: ").strip()
        if not (8 <= len(inputed_password) <= 20): # Checks if password is between 8 and 20 characters
            print("Invalid length. Your password should have between 8 and 20 characters. Try again.")
            continue

        if all(str(num) not in inputed_password for num in range(10)): # Checks if the password has any numbers
            print("Your password must include at least one number. Try again.")
            continue

        for i in special_characters: # Checks if the password has any special characters
          if i in inputed_password:
            found_special = True
        if found_special == False:
            print("Invalid password. You must use at least one special character such as !¡¿?@,._-[]{}()=/$%'<>.")
            continue

        for i in inputed_password: # Checks if the password has any capitalized characters
          if i.isupper():
            found_capitalized = True
        if found_capitalized == False:
            print("Invalid password. You must capitalize at least one character.")
            continue

        print("Valid password.")
        break

    return inputed_password

def save_user_password_salt(inputed_user, hashed_password, salt):
    sql = "INSERT INTO user_password (user, hash_salted_password, salt) VALUES (%s, %s, %s)"
    val = [inputed_user, hashed_password, salt]
    my_cursor.execute(sql, val)
    mydb.commit() # Save changes

def extract_password(inputed_user):
    sql = "SELECT salt, hash_salted_password FROM user_password WHERE user = %s"
    val = (inputed_user,)
    my_cursor.execute(sql, val)
    my_result = my_cursor.fetchall()

    if my_result:  # If data is found
        salt, hash_salted_password = my_result[0]  # Extract salt and hashed password from the first row found
        return salt, hash_salted_password
    else:
        return None, None  # Or handle the case where no data is found

# Note that the menu() function is not called, as you're supposed to do that within the code of the main.py file
