from utils import *
import requests
import json

def showRepos(username,apitoken):
    try:
        url = "https://api.github.com/users/"+username+"/repos"
        token = "Bearer "+apitoken 
        headers = {
            "Authorization": token
        }
        r = requests.get (url, headers=headers)
        p = r.json()
        q = json.dumps(p, indent=4, sort_keys=True)
        dictVal = json.loads(q)
    
        if(r.status_code == 200):
            return dictVal
        else:
            message.error ('Sorry! Try Again after entering correct credentials!')
            return False
    except:
        message.error ('Sorry! Try Again after entering correct credentials!')
        return False

showRepos("usernamehere","apitokenhere")

