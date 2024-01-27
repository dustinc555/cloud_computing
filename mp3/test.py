import requests
import json
import uuid

url = "https://seorwrpmwh.execute-api.us-east-1.amazonaws.com/prod/mp3-lexv2-autograder"

payload = {
	"graphApi": "https://gi17xjagk4.execute-api.us-east-1.amazonaws.com", #<post api for storing the graph>,
	"botId": "PHWYSFYQNB", # <id of your Amazon Lex Bot>, 
	"botAliasId": "TSTALIASID", # <Lex alias id>,
	"identityPoolId": "us-east-1:00c6fdcc-85aa-4aba-8da5-83164d335d91",#<cognito identity pool id for lex>,
	"accountId": "654654556916",
	"submitterEmail": "drcook2@illinois.edu",
	"secret": "JaTUgX1s5MzKkQTf", # <insert your secret token from coursera>,
	"region": "us-east-1"
    }

r = requests.post(url, data=json.dumps(payload))

print(r.status_code, r.reason)
print(r.text)