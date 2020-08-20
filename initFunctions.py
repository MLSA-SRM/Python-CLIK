from utils import *

def inputName():
    filename = message.prompt('Enter JSON file name (keys.json):')
    if(filename==''):
        filename = 'keys.json'
    return filename
    
def inputKeys():
    keyDict = {}
    def getKeyValue(keyName):
        key = message.prompt('Enter API key for '+keyName)
        if(key!=''):
            keyDict[keyName] = key
        elif(key==''):
            message.error('Key value cannot be empty!')
            getKeyValue(keyName)

    while(True):
        
        keyName = message.prompt('Enter API key name. Press Enter when done')
        if(keyName!=''):
            getKeyValue(keyName)

        elif (keyName==''):
            break
    
    message.success('Keys saved')
    return keyDict



print("You entered: ",inputName())
print(inputKeys())