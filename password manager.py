import json
import hashlib
def password_manager():
    password_dict = {}
    action = input("Would you like to add a new password or view existing (add/view): ")
    if action == 'add':
        site = input("Enter website: ")
        password = input("Enter password: ")
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        password_dict[site] = hashed_password
        with open('passwords.json', 'w') as f:
            json.dump(password_dict, f)
    elif action == 'view':
        site = input("Enter website to view password: ")
        with open('passwords.json', 'r') as f:
            password_dict = json.load(f)
        if site in password_dict:
            print(f"Password for {site}: {password_dict[site]}")
password_manager()
