import requests
import json

''' Fill in the following information '''
# General information
YOUR_EMAIL = "drcook2@illinois.edu" # <put your coursera account email>,
YOUR_SECRET = "3b2c848FOrO6EOKw" # <put your secret token from coursera>

# Section 1
IP_ADDRESS1 = "3.144.164.153" # <put your first EC2 instance's IP address>
IP_ADDRESS2 = "18.227.228.202" # <put your second instance's IP address>
YOUR_LOAD_BALANCER1 = "part1-1734640037.us-east-2.elb.amazonaws.com" # <put your load_balancer address for section 1>
# Section 2
YOUR_LOAD_BALANCER2 = "project1step2-1-1758533292.us-east-2.elb.amazonaws.com" # <put your load_balancer address for section 2>, 

''' Don't change the following '''
url = "https://ekwygde36j.execute-api.us-east-1.amazonaws.com/alpha/execution"
input = {
            'ip_address1': IP_ADDRESS1,
            'ip_address2': IP_ADDRESS2,
			'load_balancer1': YOUR_LOAD_BALANCER1, 
            'load_balancer2': YOUR_LOAD_BALANCER2,
			'submitterEmail': YOUR_EMAIL, 
			'secret': YOUR_SECRET, 
		}
payload = { "input": json.dumps(input),
    		"stateMachineArn": "arn:aws:states:us-east-1:913708708374:stateMachine:mp2grader"
        }

r = requests.post(url, data=json.dumps(payload))

print(r.status_code, r.reason)
print(r.text)