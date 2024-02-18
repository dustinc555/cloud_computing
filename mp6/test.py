import requests
import json

payload = {
        "USE_CACHE": "True",
        "REQUEST": "read",
        "SQLS": [1,2,3]
    }
api = "https://dley72qihej6behzdzs7xvzfqa0admcm.lambda-url.us-east-1.on.aws/"
r = requests.post(api, data=json.dumps(payload))
res = ""
print(r)
print(r.json())
res = r.json()['body']
