import sys
from examplePackage.encrypt import encryption, decryption, getKey
from examplePackage.json_convert import  jsonToDict
from examplePackage.utils import message, STORAGE_DIR, STORE_KEY_F
from examplePackage.menu_functions import add, subtract, modify
from examplePackage.helpVersion import help, version
from examplePackage.keys_init import init_function

# check encrypted
def checkEnc(filename):
    return jsonToDict(filename)

# main menu hub of CLIK
def main_menu(args = sys.argv[1:]):
    # print(args)
    if args[0].lower() == 'init':
        init_function()
    elif args[0].lower() == '--help':
        help()
    elif args[0].lower() == '--version':
        version()
    else:
        fname = args[0]
        cmd = args[1]

        # encrypt file
        if cmd.lower() == 'enc':
            if checkEnc(fname) != False:
                keyFname = message.prompt('File with key for description (' + STORAGE_DIR + '/' + STORE_KEY_F + '): ')
                key = getKey() if keyFname == '' else getKey(keyFname)
                encryption(key, fname)
                message.success(fname + ' is now encrypted')
            else:
                message.error(fname + ' is already encrypted')

        # decrypt file
        elif cmd.lower() == 'dec':
            if checkEnc(fname) != False:
                message.error(fname + ' is already decrypted')
            else:
                keyFname = message.prompt('File with key for description (' + STORAGE_DIR + '/' + STORE_KEY_F + '): ')
                key = getKey() if keyFname == '' else getKey(keyFname)
                decryption(key, fname)
                message.success(fname + ' is now decrypted')

        # add new keys
        elif cmd.lower() == 'add':
            if checkEnc(fname) != False:
                add(fname)
            else:
                message.error(fname + ' is encrypted')
        
        # subtract keys
        elif cmd.lower() == 'sub':
            if checkEnc(fname) != False:
                subtract(fname)
            else:
                message.error(fname + ' is encrypted')

        # subtract keys
        elif cmd.lower() == 'mod':
            if checkEnc(fname) != False:
                modify(fname)
            else:
                message.error(fname + ' is encrypted')


# main function
if __name__ == "__main__":
    main_menu(sys.argv[1:])
