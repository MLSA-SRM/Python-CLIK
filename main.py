from encrypt import encryption, decryption
from json_convert import  jsonToDict
from utils import message


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
        s= jsonToDict
        if(s == "False"):
            
    elif (input=="Decrypt"):
        pass
main_menu()