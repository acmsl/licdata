import os
import threading
from cryptography.fernet import Fernet


def getKey():
    local = threading.local()
    if not hasattr(local, "key"):
        local.key = os.environ["KEY"]

    return local.key


def encryptionEnabled():
    local = threading.local()
    if not hasattr(local, "encryptedFiles"):
        local.encryptedFiles = os.environ["ENCRYPTED_FILES"]

    return local.encryptedFiles


def encrypt(content):
    result = None

    if encryptionEnabled():
        fernet = Fernet(getKey())

        try:
            result = fernet.encrypt(content.encode())
        except Exception as e:
            print(f"{content} could not be encrypted: {e}")
    else:
        result = content

    return result


def decrypt(content):
    result = None

    if encryptionEnabled():
        fernet = Fernet(getKey())

        try:
            result = fernet.decrypt(content).decode()
        except Exception as e:
            print(f"{content} could not be decrypted: {e}")
    else:
        result = content

    return result


def decryptFile(file, filePath):
    result = None

    if encryptionEnabled():
        result = decrypt(file.decoded_content.decode())

    else:
        result = file.decoded_content.decode()

    return result
