import json

source = '{"user":{"name":"alice","roles":["admin","user"]}}'

data = json.loads(source)
print(data["user"]["name"], data["user"]["roles"][0])
