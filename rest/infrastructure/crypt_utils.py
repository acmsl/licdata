import os
import threading
from cryptography.fernet import Fernet


def get_key():
    local = threading.local()
    if not hasattr(local, "key"):
        local.key = os.environ["KEY"]

    return local.key


def encryption_enabled():
    local = threading.local()
    if not hasattr(local, "encryptedFiles"):
        local.encrypted_files = os.environ["ENCRYPTED_FILES"]

    return local.encrypted_files


def encrypt(content):
    result = None

    if encryption_enabled():
        fernet = Fernet(get_key())

        try:
            result = fernet.encrypt(content.encode())
        except Exception as e:
            print(f"{content} could not be encrypted: {e}")
    else:
        result = content

    return result


def decrypt(content):
    result = None

    if encryption_enabled():
        fernet = Fernet(get_key())

        try:
            result = fernet.decrypt(content).decode()
        except Exception as e:
            print(f"{content} could not be decrypted: {e}")
    else:
        result = content

    return result


def decrypt_file(file, file_path):
    result = None

    if encryption_enabled():
        result = decrypt(file.decoded_content.decode())

    else:
        result = file.decoded_content.decode()

    return result
