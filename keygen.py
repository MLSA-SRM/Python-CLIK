from cryptography.fernet import Fernet
import os
 #generating the key and storing them in a file
key = Fernet.generate_key()
#creating the key file in which the key'll be stored
file = open('key.key','wb')
file.write(key)
file.close()