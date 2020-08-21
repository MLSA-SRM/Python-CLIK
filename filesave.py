from encrypt import keygen, storeKey
from utils import message, debug, init_default_key_storage, STORAGE_DIR
from printy import raw_format
import os
from encrypt import keygen, getKey



def save():
    key= keygen()
    #Displaying the Key
    message.success("Your Security key is " + key)
    user_choice= message.prompt("Press ""Y"" to save they key")
    if(user_choice=="Y"):
        storage_choice= message.prompt("Enter the name of the file")
        if(storage_choice != ""):
            storeKey(key, storage_choice)
            
        else:
            dfile= os.path.basename(os.getcwd())
            storeKey(key, dfile)
            print(key)
    else:
        print("Your key Won't be stored! Please keep the key safe")    

    

save()    