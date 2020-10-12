from examplePackage.utils import message, debug, init_default_key_storage, printy, STORAGE_DIR, STORE_KEY_F

def help():
    message.success("Usage: clik <command> \n \n init\t\tinitializes the script to input key value pairs \n add\t\tinsert key value pair in existing json file \n sub\tdelete key value pair in existing json file \n mod\t\talter key value in existing json file \n enc\tencrypts key value dictionary to json and generate encryption key \n dec\tdecrypts json file to dictionary \n help\t\tguide through all the CLIK functions \n version\tshows the CLIK version installed ")

def version():
    message.success("CLIK Version 0.0.0")


#test functions
#help()
#version()