# FingerPrintDB
Scripts to run on db server and raspberry pi

Make sure MySQL is running (xampp) on port 3306.

Execute the "createdb.py" in the server initially to create a database.

Run "server_script.py" to accept fingerprint info sent by raspberry pi to complete transactions, and to register sellers from web server to the database.

Inside the raspberry pi script add "raspberry_script.py" to send fingerprint info to server.

In the web server run "seller_register.py" to register seller into database.
