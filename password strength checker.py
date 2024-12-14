import re
def password_strength(password):
    if len(password) < 8:
        return "Weak"
    if not re.search("[a-z]", password):
        return "Weak"
    if not re.search("[A-Z]", password):
        return "Weak"
    if not re.search("[0-9]", password):
        return "Weak"
    return "Strong"

password = input("Enter a password: ")
print(f"Password strength: {password_strength(password)}")
