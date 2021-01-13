from clikpython.utils import message, debug, init_default_key_storage, printy, STORAGE_DIR, STORE_KEY_F

def help():
     message.success("Usage: clik <command> \n \n init\t\tinitializes the script to input key value pairs \n add\t\tinsert key value pair in existing json file, clik <name of file> add\n sub\t\tdelete key value pair in existing json file, clik <name of file> sub \n mod\t\talter key value in existing json file, clik <name of file> mod\n enc\t\tencrypts key value dictionary to json and generate encryption key, clik <name of file> enc\n dec\t\tdecrypts json file to dictionary, clik <name of file> dec\n help\t\tguide through all the CLIK functions \n version\tshows the CLIK version installed ")
def version():
    message.success("CLIK Version 1.0")


#test functions
#help()
#version()
