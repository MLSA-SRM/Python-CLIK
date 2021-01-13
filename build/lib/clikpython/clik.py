import os
import sys
from clikpython.encrypt import encryption, decryption, getKey
from clikpython.json_convert import  jsonToDict
from clikpython.utils import message, STORAGE_DIR, STORE_KEY_F
from clikpython.menu_functions import add, subtract, modify
from clikpython.helpVersion import help, version
from clikpython.keys_init import init_function

# check encrypted
def checkEnc(filename):
    return jsonToDict(filename)

# main menu hub of CLIK
def main_menu(args=sys.argv[1:]):
    if len(args) == 0:
        help()
    else:
        if args[0].lower() == 'init':
            init_function()
        elif args[0].lower() == '--help':
            help()
        elif args[0].lower() == '--version':
            version()
        elif len(args) == 2:
            fname = args[0]

            # check if file exists
            if not os.path.isfile(fname):
                message.error(f'{fname} not found')
                help()
                return

            cmd = args[1]

            # encrypt file
            if cmd.lower() == 'enc':
                if checkEnc(fname) != False:
                    shouldLoad = message.prompt('Load key from memory? (Y/n): ')
                    if shouldLoad.lower() == 'y' or shouldLoad.lower() == '':
                        keyFname = message.prompt('File with key for decryption (' + STORAGE_DIR + '/' + STORE_KEY_F + '): ')
                        key = getKey() if keyFname == '' else getKey(keyFname)
                    elif shouldLoad.lower() == 'n':
                        key = message.prompt('Key for encryption: ')
                    encryption(key, fname)
                else:
                    message.error(fname + ' is already encrypted')

            # decrypt file
            elif cmd.lower() == 'dec':
                if checkEnc(fname) != False:
                    message.error(fname + ' is already decrypted')
                else:
                    shouldLoad = message.prompt('Load key from memory? (Y/n): ')
                    if shouldLoad.lower() == 'y' or shouldLoad.lower() == '':
                        keyFname = message.prompt('File with key for decryption (' + STORAGE_DIR + '/' + STORE_KEY_F + '): ')
                        key = getKey() if keyFname == '' else getKey(keyFname)
                    elif shouldLoad.lower() == 'n':
                        key = message.prompt('Key for decryption: ')
                    decryption(key, fname)

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
            
            # invalid arguments
            else:
                message.error('Invalid Argument')
                help()
        # invalid arguments
        else:
            message.error('Invalid Argument')
            help()

# main function
if __name__ == "__main__":
    main_menu(sys.argv[1:])
