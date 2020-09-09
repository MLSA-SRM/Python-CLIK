from encrypt import encryption, decryption
from json_convert import  jsonToDict
from utils import message
from keys_init import get_filename_from_user, generate_encryption

def main_menu():
    message.success("1)Type  ""add"" to add a key to the existing API keys. \n Type ""sub"" to Subtract a key to the existing API keys. \n Type ""mod"" to modify your Api keys \n Type ""Encrypt"" to Encrypt your Keys \n Type ""Decrypt"" to decrypt your keys")
    input= message.prompt("Enter your choice")
    if(input=="add"):
        pass
    elif (input=="sub"):
        pass
    elif (input=="mod"):
        pass
    elif (input=="Encrypt"):
        filename= get_filename_from_user()
        key= generate_encryption()
        s= jsonToDict(filename)
       
        if(s == False):
            print("The data is  encrypted")
        else:
            print("The data was not encrypted")
            encryption(key, filename)
            #print("The Json is now encrypted")    
            
    elif (input=="Decrypt"):
        filename= get_filename_from_user()
        
        s= jsonToDict(filename)
        print(s)
        if(s == False):
            print("The data is  encrypted")
            key1=message.prompt("enter the key")
            decryption(key1, filename)

        else:
            print("The data is not encrypted")
          
        
main_menu()
