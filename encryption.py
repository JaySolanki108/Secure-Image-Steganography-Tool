from cryptography.fernet import Fernet
import os

KEY_FILE = "secret.key"


def load_key():
    if not os.path.exists(KEY_FILE):
        key = Fernet.generate_key()
        with open(KEY_FILE, "wb") as f:
            f.write(key)

    with open(KEY_FILE, "rb") as f:
        return f.read()


def encrypt_message(message):
    key = load_key()
    fernet = Fernet(key)
    return fernet.encrypt(message.encode()).decode()


def decrypt_message(message):
    key = load_key()
    fernet = Fernet(key)
    return fernet.decrypt(message.encode()).decode()