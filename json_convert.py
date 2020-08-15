import json

#sample api keys
api_val = {'ADMIN_KEY':'exampleadmin123',
'ADMIN_USERNAME':'example@admin',
'ADMIN_PASSWORD':'Darwin@Example2506',
'TWITTER_ACCESS_TOKEN':'1234614-4Du6ZlFtVOpNMgtwIKjRe4wzwxHejcDRaxjNmAU',
'INSTA_API_KEY':'Qhsh6yihijy3e8',
'YOUTUBE_API_KEY':'83nicciwdcIIUNij',
'FACEBOOK_API_KEY_SECRET':'7jewkdjwenbnsH',
'INSTA_API_KEY_SECRET':'Qhsh6fjkdsbfky3e8',
'YOUTUBE_API_KEY_SECRET':'8djkfhjsndcIIUNij',
'FACEBOOK_API_KEYS_SECRET':'7jewdsjnfdnjnfssnsH'}

#function to convert JSON to dictionary and print
def jsonTodict(fn1):
    with open(fn1,'r') as fh:
        json_str = fh.read()
        json_value = json.loads(json_str)
        print(json_value)


#function to convert dictionary to JSON 
def dictTojson(apidict,fn2):
    try:
        with open(fn2,'w') as fh2:
            fh2.write(json.dumps(apidict, indent=4, sort_keys=True))
            print("\n[TRUE] API Keys dictionary written as json successfully!")
    except Exception as e:
        print("\n[FALSE] Some error occured!")
        print(e)
    

#calling the functions
jsonTodict('test_data/apikeys.json')
dictTojson(api_val,'test_data/apikeys2.json')
