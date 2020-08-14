import json

api_val = {'ADMIN_KEY':'exampleadmin123',
'ADMIN_USERNAME':'example@admin',
'ADMIN_PASSWORD':'Darwin@Example2506',
'TWITTER_ACCESS_TOKEN':'1234614-4Du6ZlFtVOpNMgtwIKjRe4wzwxHejcDRaxjNmAU',
'INSTA_API_KEY':'Qhsh6yihijy3e8',
'YOUTUBE_API_KEY':'83nicciwdcIIUNij',
'FACEBOOK_API_KEY_SECRET':'7jewkdjwenbnsH'}

with open('apikeys.json','w') as fh:
    fh.write(json.dumps(api_val, indent=4,sort_keys=True))
print("API keys written in JSON Successfully")


print()
print("Reading values from JSON file:")
with open('apikeys2.json','r') as fh2:
    json_str = fh2.read()
    json_value = json.loads(json_str)
    print(json_value)
