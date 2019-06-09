#Accepts transaction req from fingerprint sensor and registers users into database
from flask import Flask, request, jsonify
import mysql.connector
app = Flask(__name__)
@app.route('/pitransactionrequest', methods=['POST'])
def pi():
	mydb = mysql.connector.connect(
	  host="localhost",
	  user="root",
	  passwd="",
	  database="fingerdb"
	)
	mycursor = mydb.cursor()
	
	userpass = request.json
	sql_query = "SELECT * FROM sellers"
	mycursor.execute(sql_query)
	myresult = mycursor.fetchall()
	for i in myresult:
		if i[0]==userpass[0]:
			if i[1]==userpass[1]:
				fingerdata = userpass[2]
				money = userpass[3]
				#Use this finger data and money for transaction further....
				return jsonify("Transaction complete")
			else:
				return jsonify("Wrong password")
	return jsonify("Seller not Registered")

@app.route('/piregisterseller', methods=['POST'])
def pi2():
	mydb = mysql.connector.connect(
	  host="localhost",
	  user="root",
	  passwd="",
	  database="fingerdb"
	)
	mycursor = mydb.cursor()
	
	userpass = request.json
	sql = "INSERT INTO sellers (userid, password, bankdet) VALUES (%s, %s,%s)"
	val = (userpass[0], userpass[1],userpass[2])
	mycursor.execute(sql, val)

	mydb.commit()
	return jsonify("Seller Registered")
@app.route('/piregisterbuyeracc', methods=['POST'])
def pi3():
	mydb = mysql.connector.connect(
	  host="localhost",
	  user="root",
	  passwd="",
	  database="fingerdb"
	)
	mycursor = mydb.cursor()
	
	userpass = request.json
	sql = "INSERT INTO buyers (userid, password, bankdet) VALUES (%s, %s,%s)"
	val = (userpass[0], userpass[1],userpass[2])
	mycursor.execute(sql, val)

	mydb.commit()
	return jsonify("Buyer's account Registered, Please register buyer's finger in any seller's fingerprint sensor")
@app.route('/piregisterbuyerfinger', methods=['POST'])
def pi4():
	mydb = mysql.connector.connect(
	  host="localhost",
	  user="root",
	  passwd="",
	  database="fingerdb"
	)
	mycursor = mydb.cursor()
	
	userpass = request.json
	sql_query = "SELECT * FROM buyers"
	mycursor.execute(sql_query)
	myresult = mycursor.fetchall()
	for i in myresult:
		if i[0]==userpass[0]:
			if i[1]==userpass[1]:
				sql_query="UPDATE buyers SET finger = %s WHERE userid = %s"
				val = (userpass[2],userpass[0])
				mycursor.execute(sql_query, val)
				mydb.commit()
				return jsonify("Buyer's finger registered, now you can make transactions")
			else:
				return jsonify("Wrong password")
	return jsonify("Buyer not registered in web server")


	mydb.commit()
	return jsonify("Seller Registered")
@app.route('/checkall', methods=['POST'])
def pi5():
	mydb = mysql.connector.connect(
	  host="localhost",
	  user="root",
	  passwd="",
	  database="fingerdb"
	)
	mycursor = mydb.cursor()
	userpass = request.json
	sql_query = "SELECT * FROM sellers"
	mycursor.execute(sql_query)
	myresult = mycursor.fetchall()
	for i in myresult:
		print(i)
	sql_query = "SELECT * FROM buyers"
	mycursor.execute(sql_query)
	myresult = mycursor.fetchall()
	for i in myresult:
		print(i)
	return jsonify("Cowbunga it is")
if __name__ == '__main__':
    app.run(debug=True)
