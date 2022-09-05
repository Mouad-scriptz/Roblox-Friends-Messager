import requests
headers={"accept":"application/json","content-type":"application/json","cookie":f".ROBLOSECURITY={open('cookie.txt','r').read()}","x-csrf-token": requests.post("https://auth.roblox.com/v2/logout", cookies={".ROBLOSECURITY": open('cookie.txt', 'r').read()}).headers["x-csrf-token"]}
for x in requests.get("https://chat.roblox.com/v2/get-user-conversations?pageNumber=1&pageSize=100", headers=headers).json(): req = requests.post("https://chat.roblox.com/v2/send-message", headers=headers, json={"conversationId": x['id'],"message": "hi"})
