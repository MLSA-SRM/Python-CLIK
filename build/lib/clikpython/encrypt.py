from clikpython.utils import message, debug, init_default_key_storage, STORAGE_DIR, STORE_KEY_F
from printy import raw_format
from cryptography.fernet import Fernet
import os

# generating encryption key
def keygen():
    try:
        #generating the key and storing them in a file
        key = Fernet.generate_key()
        message.success("Encryption key generated successfully")
    except Exception as e:
        message.error('Couldn\'t generate encryption key')
        debug.error(str(e))
        return False
    return key.decode('utf-8')

# storing the generated key to default/specified filename
def storeKey(key, filename = STORE_KEY_F):
    storeTo = os.path.join (STORAGE_DIR, filename) + "_keys.key"
    if init_default_key_storage():
        try:
            #creating the key file in which the key'll be stored
            file = open(storeTo,'w')
            file.write(key)
            file.close()
            message.success("Key was stored to " + storeTo + " successfully")
        except Exception as e:
            message.error("Key couldn't be stored to " + storeTo)
            debug.error("Key couldn't be stored to " + storeTo)
            return False
        return True
    else:
        return False

# retrieve key from specified filename
def getKey(filename = STORE_KEY_F):
    getFrom = os.path.join (STORAGE_DIR, filename) + "_keys.key"
    if init_default_key_storage():
        try:
            # retriving key file
            file = open (getFrom, 'r')
            key = file.read ()
            file.close ()
            message.success ('Loaded encryption key successfully')
            return key
        except:
            message.error ('Couldn\'t load encryption key')
            debug.error ('Couldn\'t load encryption key')
            return False
    else:
        message.error ('Couldn\'t load encryption key')
        debug.error ('Couldn\'t load encryption key')
        return False

# encrypting file using key
def encryption(key, filename):
    try:
        with open(filename, 'rb') as f:
            data = f.read()
        #encrypting the data from the given file name
        fernet = Fernet(key)
        encrypted=fernet.encrypt(data)    
        with open(filename,'wb') as f:
            f.write(encrypted)
        message.success(filename + ' successfully encrypted')
    except Exception as e:
        message.error(filename + ' couldn\'t be encrypted')
        debug.error(filename + ' couldn\'t be encrypted')
        print (e)
        return False
    return True

# decrypting file using key
def decryption(key, filename):
    try:
        with open(filename,'rb') as f:
            data = f.read()
        q = Fernet(key)
        decrypted_message = q.decrypt(data)
        with open(filename,'wb') as f:
            f.write(decrypted_message)
        message.success(filename + ' successfully decrypted')
    except Exception as e:
        message.error(filename + ' couldn\'t be decrypted')
        debug.error(filename + ' couldn\'t be decrypted')
        print(e)
        return False
    return True

# test functions
#print(storeKey(keygen()))
#encryption(getKey(), 'test_data/test_api_keys.json')
#decryption(getKey(), 'test_data/test_api_keys.json')
