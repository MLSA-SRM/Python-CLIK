import requests
import json

def showRepos(username,apitoken):
    try:
        url = "https://api.github.com/users/"+username+"/repos"
        token = "Bearer "+apitoken 
        headers = {"Authorization": token}
        r = requests.get (url, headers=headers)
        p = r.json()
        q = json.dumps(p, indent=4, sort_keys=True)
        dictVal = json.loads(q)
        print(r)
        print(type(dictVal))
        print(dictVal)
       
    except:
        print("Sorry! Try again after passing correct information!")
        return False

showRepos("usernamehere","personalaccesstokenhere")
