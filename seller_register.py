# This script needs to be run in the web server to register the user in database server
import requests
username = 'testuser'
password = 'testpass'
response = requests.post('http://127.0.0.1:5000/piregister', json=(username,password)) #Change server IP
if response.ok:
    print(response.json())