# This script needs to be run in the web server to register the user in database server
import requests
username = 'testseller'
password = 'testpass'
bank_details = 'acc-no'
response = requests.post('http://127.0.0.1:5000/piregisterseller', json=(username,password,bank_details)) #Change server IP
if response.ok:
    print(response.json())
