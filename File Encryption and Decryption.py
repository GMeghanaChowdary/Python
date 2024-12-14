from cryptography.fernet import Fernet
def generate_key():
    return Fernet.generate_key()
def encrypt_file(file_name, key):
    with open(file_name, 'rb') as file:
        data = file.read()
    fernet = Fernet(key)
    encrypted = fernet.encrypt(data)
    with open(file_name + '.enc', 'wb') as file:
        file.write(encrypted)
def decrypt_file(file_name, key):
    with open(file_name, 'rb') as file:
        encrypted = file.read()
    fernet = Fernet(key)
    decrypted = fernet.decrypt(encrypted)
    with open(file_name.replace('.enc', ''), 'wb') as file:
        file.write(decrypted)
key = generate_key()
encrypt_file("sample.txt", key)
decrypt_file("sample.txt.enc", key)
