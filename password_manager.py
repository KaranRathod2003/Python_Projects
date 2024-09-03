# from cryptography.fernet import Fernet


# '''
# def write_key():
#     key = Fernet.generate_key()
#     with open ('key.key', 'wb') as key_file:
#         key_file.write(key)'''

# # write_key()
# def load_key():
#     file = open("key.key", 'rb')
#     key  = file.read()
#     file.close()
#     return key



# master_pwd = input("Enter a master passward: ")
# key = load_key() + master_pwd.encode()
# fer = Fernet(key)




# def view():
#     with open ('passwords.txt', 'r') as f:
#         for line in f.readlines():
#             data = line.rstrip()
#             user, passw = data.split("|")
#             print("Username:", user, "|", "Password:", fer.decrypt(passw.encode()).decode() )

# def add():
#     name = input("Enter Account name: ")
#     pwd = input("Enter your password: ")

#     with open('passwords.txt', 'a') as f:
#         f.write( name + "|"+ fer.encrypt(pwd.encode()).decode() + "\n")

# while True:
#     mode = input("Enter the following choices [view: list existing password, add:to add new passward, q:to quit] ").lower()
#     if mode == "q":
#         break

#     if mode == "view":
#         view()
#     elif mode == "add":
#         add()
#     else:
#         print("Invalid mode.")
#         continue




from cryptography.fernet import Fernet

# Function to generate a new encryption key and store it in a file
# This function is commented out since the key should only be generated once
'''
def write_key():
    key = Fernet.generate_key()
    with open('key.key', 'wb') as key_file:
        key_file.write(key)
'''

# Function to load the existing encryption key from the file
def load_key():
    # Open the key file in binary read mode
    file = open("key.key", 'rb')
    key = file.read()
    file.close()
    return key

# Prompt the user to enter a master password
master_pwd = input("Enter a master password: ")

# Load the encryption key and combine it with the master password
key = load_key() + master_pwd.encode()

# Create a Fernet encryption object with the combined key
# Note: This line will raise an error due to the incorrect key length
fer = Fernet(key)  # This line will fail because the key length is incorrect

# Function to view stored usernames and passwords
def view():
    with open('passwords.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split("|")
            # Decrypt the stored password and display it along with the username
            print("Username:", user, "|", "Password:", fer.decrypt(passw.encode()).decode())

# Function to add a new username and password
def add():
    name = input("Enter Account name: ")
    pwd = input("Enter your password: ")

    with open('passwords.txt', 'a') as f:
        # Encrypt the password and store it with the username
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")

# Main loop to handle user commands
while True:
    mode = input("Enter the following choices [view: list existing passwords, add: to add new password, q: to quit] ").lower()
    if mode == "q":
        break

    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode.")
        continue
