from cryptography.fernet import Fernet
import os

def keygen():
    from cryptography.fernet import Fernet
    #generating the key and storing them in a file
    key = Fernet.generate_key()
    #creating the key file in which the key'll be stored
    file = open('key.key','wb')
    file.write(key)
    file.close()

 



def encyption():

    #taking key as user input
    key1= input("enter the encyption key")

    with open('test_data/apikeys.json','rb') as f:
        data = f.read()

    #encrypting the data from the given file name

    fernet = Fernet(key1)
    encrypted=fernet.encrypt(data)    
    os.remove('test_data/apikeys.json') #deleting the file with the original api key

    with open('new.json','wb') as f:
        f.write(encrypted)

def decrypt():
    key1= input("enter the encyption key")
    with open('new.json','rb') as f:
        data = f.read()
    q= Fernet(key1)
    decrypted_message = q.decrypt(data)

    with open('decrypted.json','wb') as f:
        f.write(decrypted_message)

keygen()   
encyption()
decrypt()



 