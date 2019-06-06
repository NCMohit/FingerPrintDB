# Add this to the raspberry pi script to send fingerprint info to server
import requests
 
data_from_pi = 'Changeme (Fingerprint data)'
userid = 1
response = requests.post('http://127.0.0.1:5000/pi', json=(data_from_pi,userid)) #Change server IP
if response.ok:
    print(response.json())