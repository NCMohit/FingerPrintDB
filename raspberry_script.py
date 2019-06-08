# Add this to the raspberry pi script to send fingerprint info to server
import requests
#Finger for buyer identification, userpass for seller identification
finger = 'Changeme (Fingerprint data)'
username = 'cyka'
password = 'blyat1'
response = requests.post('http://127.0.0.1:5000/pitransactionrequest', json=(username,password,finger)) #Change server IP
if response.ok:
    print(response.json())
