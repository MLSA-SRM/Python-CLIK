from clikpython.utils import message, debug, init_default_key_storage, printy, STORAGE_DIR, STORE_KEY_F
from clikpython.json_convert import jsonToDict, dictToJson, display_json


def add(fileName):
    dictkeys = jsonToDict(fileName)

    def getKeyValue(keyName):
        key = message.prompt(keyName + ' value')
        if(key!=''):
            dictkeys[keyName] = key
        elif(key==''):  
            message.error('Value cannot be empty.')
            getKeyValue(keyName)
    
    while(True):
        keyName = message.prompt('Key (done)')
        if(keyName!=''):
            getKeyValue(keyName)
        elif (keyName==''):
            break
    try:
        dictToJson(dictkeys, fileName)
        message.success('New keys added successfully!')
    except:
        message.error('Some error occured!')
        return False


def subtract(fileName):
    dictkeys = jsonToDict(fileName)

    def removeKeyValue(keyName):
        try:
            del dictkeys[keyName]
        except:
            message.error('No such Key exists!')
        

    while(True):
        keyName = message.prompt('Enter Key to be removed (done)')
        if(keyName!=''):
            removeKeyValue(keyName)
        elif (keyName==''):
            break
    
    try:
        dictToJson(dictkeys, fileName)
        message.success('Keys removed successfully!')
    except:
        message.error('Some error occured!')
        return False
    

def modify(fileName):
    dictkeys = jsonToDict(fileName)

    def modifyKeyValue(keyName):
        if keyName in dictkeys:
            key = message.prompt(keyName + ' new value')
            if(key!=''):
                dictkeys[keyName] = key
            elif(key==''):  
                message.error('Value cannot be empty.')
                getKeyValue(keyName)

        else:
            message.error('No such Key exists!')

    while(True):
        keyName = message.prompt('Enter Key to be modified (done)')
        if(keyName!=''):
            modifyKeyValue(keyName)
        elif (keyName==''):
            break
    
    try:
        dictToJson(dictkeys,fileName)
        message.success('Keys modified successfully!')
    except:
        message.error('Some error occured!')
        return False
    



#test functions

#add(fileName)
#subtract(fileName)
#modify(fileName)