from printy import printy, inputy
import os
import sys

# Mode Variables---------------------------
DEBUG_MODE = True
STORAGE_DIR = os.path.expanduser ('~/clik-safety-keys')
STORE_KEY_F = os.path.basename(os.getcwd())
#------------------------------------------

# class for handling CLI messages
class _message:

    # CLI message for success
    def success (self, msg):
        printy ('[n]\[clik:suc\]@ ' + msg)
    
    # CLI message for debug
    def error (self, msg):
        printy ('[r]\[clik:err\]@ ' + msg)
    
    # CLI prompt for input
    def prompt (self, msg):
        thisInput = inputy ('[c]\[clik:prt\]@ ' + msg + '> ')
        return thisInput
    
    def delete_last (self):
        sys.stdout. write("\033[F") #back to previous line.
        sys.stdout. write("\033[K") #clear line.

# class for handling development debugging
class _debug:

    # set mode for display or not
    def __init__ (self, mode=False):
        self.mode = mode

    # debug message for success
    def success (self, msg):
        if self.mode:
            printy ('[n]\[debug:suc\]@ ' + msg)
    
    # debug message for error
    def error (self, msg):
        if self.mode:
            printy ('[r]\[debug:err\]@ ' + msg)

    # prompt for input
    def prompt (self, msg):
        if self.mode:
            thisInput = inputy ('[c]\[debug:prt\]@ ' + msg + '> ')
            return thisInput

# init objects for import 
message = _message ()
debug = _debug (DEBUG_MODE)

def init_default_key_storage ():
    storageInit = os.path.join (STORAGE_DIR, '/readme.txt')
    if os.path.exists (STORAGE_DIR):
        message.success ('Default key storage is initialised at ' + STORAGE_DIR)
    else:
        try:
            os.mkdir (STORAGE_DIR)
            message.success ('Default key storage initialised at ' + STORAGE_DIR)
        except Exception as e:
            message.error ('Default key storage directory couldn\'t be initialised at ' + STORAGE_DIR)
            debug.error ('couldn\'t create directory for storage')
            return False
        return True
    return True

# test functions
#message.success ('This is in green  ')
#message.error ('This is in red')
#message.prompt ('This is in blue')

#debug.success ('Yep')
#debug.error ('Nope')
#debug.prompt ('Prompt')

# print(init_default_key_storage())
