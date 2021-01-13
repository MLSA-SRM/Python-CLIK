import json
from clikpython.utils import message, debug, printy

#sample api keys
api_val = {
    'ADMIN_KEY':'exampleadmin123',
    'ADMIN_USERNAME':'example@admin',
    'ADMIN_PASSWORD':'Darwin@Example2506',
    'TWITTER_ACCESS_TOKEN':'1234614-4Du6ZlFtVOpNMgtwIKjRe4wzwxHejcDRaxjNmAU',
    'INSTA_API_KEY':'Qhsh6yihijy3e8',
    'YOUTUBE_API_KEY':'83nicciwdcIIUNij',
    'FACEBOOK_API_KEY_SECRET':'7jewkdjwenbnsH',
    'INSTA_API_KEY_SECRET':'Qhsh6fjkdsbfky3e8',
    'YOUTUBE_API_KEY_SECRET':'8djkfhjsndcIIUNij',
    'FACEBOOK_API_KEYS_SECRET':'7jewdsjnfdnjnfssnsH'
}

#function to convert JSON to dictionary and print
def jsonToDict(filename):
    try:
        with open(filename,'r') as fh:
            json_str = fh.read()
            json_value = json.loads(json_str)
        return json_value
    except:
        return False


#function to convert dictionary to JSON 
def dictToJson(inputDict, filename, indents=2):
    try:
        with open(filename, 'w') as fh2:
            fh2.write(json.dumps(inputDict, indent=indents, sort_keys=True))
        message.success('Keys stored successfully')
        return True 
    except Exception as e:
        message.error('Couldn\'t write to JSON')
        debug.error(str(e))
        return False

# function to format and display JSON data
def display_json (filename, display_indent=4):
    json_val = jsonToDict(filename)
    if json_val:
        message.success(filename + ' loaded successfully')
        printy (json_val, indentation=display_indent)
    else:
        message.error('JSON couldn\'t be loaded')
        debug.error('JSON to Dict Failed')

#calling the functions

#print(jsonToDict('test_data/test_api_keys.json'))
# dictToJson(api_val,'test_data/test_api_keys.json')
#display_json ('test_data/test_api_keys.json')
