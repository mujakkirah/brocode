# Validate user input exercise
# 1. username is no more than 12 characters
# 2. username must not contain spaces
# 3. username must not contain digits


# 1. username is no more than 12 characters
username = input("Enter your user name: ")

if len(username) > 12:
    print("Your Username can't be more than 12 characters")
else:
    print(f"Welcome {username}")

# 2. username must not contain spaces #find method
username = input("Enter your user name: ")

if len(username) > 12:
    print("Your Username can't be more than 12 characters")
elif not username.find(" ") == -1:
    print(" your username must not contain spaces")
else:
    print(f"Welcome {username}")



# 3. username must not contain digits #username.isalpha()
username = input("Enter your user name: ")

if len(username) > 12:
    print("Your Username can't be more than 12 characters")
elif not username.find(" ") == -1:
    print(" your username must not contain spaces")
elif not username.isalpha ():
    print("Your username must not contain digits")
else:
    print(f"Welcome {username}")
