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
				#Use this finger data for transaction further....
				return jsonify("Transaction complete")
			else:
				return jsonify("Wrong password")
	return jsonify("User not Registered")

@app.route('/piregister', methods=['POST'])
def pi2():
	mydb = mysql.connector.connect(
	  host="localhost",
	  user="root",
	  passwd="",
	  database="fingerdb"
	)
	mycursor = mydb.cursor()
	
	userpass = request.json
	sql = "INSERT INTO sellers (userid, password) VALUES (%s, %s)"
	val = (userpass[0], userpass[1])
	mycursor.execute(sql, val)

	mydb.commit()
	return jsonify("User Registered")	
if __name__ == '__main__':
    app.run(debug=True)
