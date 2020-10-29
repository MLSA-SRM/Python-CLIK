from clikpython.utils import message, debug, init_default_key_storage, printy, STORAGE_DIR, STORE_KEY_F
from clikpython.encrypt import os, keygen, storeKey, encryption
from clikpython.json_convert import dictToJson

# function to get filename for holding keys from user
def get_filename_from_user():
    filename = message.prompt('Name of file holding keys (keys.json)')

    # default input: keys.json
    if(filename==''):
        filename = 'keys.json'

    return filename
    
# function to get keys from the user
def get_keys_from_user():
    keyDict = {}

    # get value
    def getKeyValue(keyName):
        key = message.prompt(keyName + ' value')
        if(key!=''):
            keyDict[keyName] = key
        elif(key==''):
            message.error('Value cannot be empty.')
            getKeyValue(keyName)
    
    # get key
    while(True):
        keyName = message.prompt('Key (done)')
        if(keyName!=''):
            getKeyValue(keyName)
        elif (keyName==''):
            break
    
    # default input ends key-value input sequence
    message.delete_last()
    return keyDict

# function to generate and save encryption key
def generate_encryption():
    key = keygen()

    #Displaying the Key
    message.success("SECURITY KEY GENERATED: " + key)
    user_choice = message.prompt("Save the key locally (Y/n)")

    # user choice to save the file
    # default user choice is YES
    if user_choice == "" or user_choice.lower() == "y" or user_choice.lower() == "yes":
        storage_choice = message.prompt("Path to store key to (" + os.path.join (STORAGE_DIR, STORE_KEY_F) + "_keys.key" + ")")
        if storage_choice != "":
            storeKey(key, storage_choice)
        else:
            storeKey(key)
            print(key)
    elif user_choice.lower()=="n" or user_choice.lower()=="no":
        message.success("YOUR KEY WILL NOT BE STORED. KEEP IT SAFE.")
    else:
        message.error("INVALID INPUT")
        generateEncryption()
    return key

# clik init
def init_function():
    if init_default_key_storage():
        filename = get_filename_from_user()
        tokendict = get_keys_from_user()
        enc_key = generate_encryption()

        if dictToJson(tokendict, filename):
            if encryption(enc_key, filename):
                message.success("Filename: " + filename)
        else:
            message.error("Filename: " + filename)
        message.success("Keys Added: ")
        printy(tokendict, indentation=4)


# init_function()