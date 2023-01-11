from cryptography.fernet import Fernet


def getKey():
    if not local.key:
        local.key = os.environ["KEY"]

    return local.key


def encrypt(content):
    result = None

    fernet = Fernet(getKey())

    try:
        result = fernet.encrypt(content.encode())
    except:
        print(f"{content} could not be encrypted")

    return result


def decrypt(content):
    result = None
    fernet = Fernet(getKey())

    try:
        result = fernet.decrypt(content).decode()
    except:
        print(f"{content} could not be decrypted")

    return result


def decryptFile(file, filePath):
    result = None

    decFile = decrypt(file.decoded_content.decode())

    if decFile:
        result = decFile.decode()
    else:
        print(f"{filePath} could not be decrypted")

    return result
