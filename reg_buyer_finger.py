# This script needs to be added in the raspberry pi to register the buyer's finger in database server
import requests
username = 'testbuyer'
password = 'testpass'
finger = 'Finger from raspberry-pi'
response = requests.post('http://127.0.0.1:5000/piregisterbuyerfinger', json=(username,password,finger)) #Change server IP
if response.ok:
    print(response.json())