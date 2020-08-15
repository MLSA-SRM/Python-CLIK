from cryptography.fernet import Fernet
import os
 

#taking key as user input
key1= input("enter the encyption key")

with open('test_data/apikeys2.json','rb') as f:
    data = f.read()

#encrypting the data from the given file name

fernet = Fernet(key1)
encrypted=fernet.encrypt(data)    
os.remove('test_data/apikeys2.json') #deleting the file with the original api key

with open('new.json','wb') as f:
    f.write(encrypted)

 