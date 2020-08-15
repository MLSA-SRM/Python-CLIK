from cryptography.fernet import Fernet
import os

key1= input("enter the encyption key")
with open('new.json','rb') as f:
    data = f.read()
    q= Fernet(key1)
decrypted_message = q.decrypt(data)

with open('decrypted.json','wb') as f:
    f.write(decrypted_message)