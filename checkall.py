#script to check all buyers and users
import requests
response = requests.post('http://127.0.0.1:5000/checkall', json="Cowbunga") #Change server IP
if response.ok:
    print(response.json())