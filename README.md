# FingerPrintDB
Scripts to run on db server and raspberry pi

Make sure MySQL is running (xampp) on port 3306.

Execute the "createdb.py" in the server initially to create a database.

Run "server_script.py" to accept fingerprint info sent by raspberry pi to complete transactions, and to register sellers and buyer from web server to the database.

Inside the raspberry pi script add "raspberry_script.py" to make transaction between buyer and seller, and add "reg_buyer_finger.py" to register buyer's finger into database.

In the web server run "seller_register.py" to register seller into database, "reg_buyer_acc.py" to register buyer's account in database.
