
from encrypt import encryption, decryption
from json_convert import  jsonToDict
from utils import message
from keys_init import get_filename_from_user, generate_encryption
from menu_functions import add, subtract, modify
from helpVersion import help, version

def main_menu():
    message.success("1)Type  ""add"" to add a key to the existing API keys. \n Type ""sub"" to Subtract a key to the existing API keys. \n Type ""mod"" to modify your Api keys \n Type ""Encrypt"" to Encrypt your Keys \n Type ""Decrypt"" to decrypt your keys \n Type ""help""to get help\n Type ""version"" to know the current version")
    input= message.prompt("Enter your choice")
    filename= message.prompt("Enter file name")
    if(input=="add"):
        s= jsonToDict(filename)
        if(s == False):
            key1=message.prompt("enter the key")
            decryption(key1, filename)
            add(filename)
            encryption(key1, filename)
        else:
            add(filename)
    elif (input=="sub"):
        s= jsonToDict(filename)
        if(s == False):
            key1=message.prompt("enter the key")
            decryption(key1, filename)
            subtract(filename)
            encryption(key1, filename)
        else:
            subtract(filename)
    elif (input=="mod"):
        s= jsonToDict(filename)
        if(s == False):
            key1=message.prompt("enter the key")
            decryption(key1, filename)
            modify(filename)
            encryption(key1, filename)
        else:
            modify(filename)
                
    elif (input=="Encrypt"):
        s= jsonToDict(filename)
                
        if(s == False):
            message.success("The data is  encrypted")
        else:
            key1=message.prompt("enter the key")
            message.success("The data was not encrypted")
            encryption(key1, filename)
            #print("The Json is now encrypted")
                
    elif (input=="Decrypt"):
        s= jsonToDict(filename)
                
        if(s == False):
            key1=message.prompt("enter the key")
            decryption(key1, filename)
                    
        else:
            message.success("The data is not encrypted")
    elif(input=="help"):
        help()
    elif(input=="version"):
        version()
main_menu()
