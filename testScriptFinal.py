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
        info = str(r)
       
        repCode = "<Response [200]>"
        
        if(info==repCode):
            return dictVal
        else:
            print("Sorry! Try again after passing correct credentials!")
            return False
       
    except:
        print("Sorry! Try again after passing correct credentials!")
        return False

showRepos("usernamehere","personalaccesstokenhere")

