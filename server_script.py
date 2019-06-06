from flask import Flask, request, jsonify
import mysql.connector
app = Flask(__name__)
@app.route('/pi', methods=['POST'])
def pi():
	mydb = mysql.connector.connect(
	  host="localhost",
	  user="root",
	  passwd="",
	  database="fingerdb"
	)
	mycursor = mydb.cursor()
	
	pi_data = request.json

	sql = "INSERT INTO fingers (finger, userid) VALUES (%s, %s)"
	val = (pi_data[0], pi_data[1])
	mycursor.execute(sql, val)

	mydb.commit()  
	print("Database: ")
	mycursor.execute("SELECT * FROM fingers")
	myresult = mycursor.fetchall()

	for x in myresult:
		print(x) 
    
	return jsonify(pi_data)
 
if __name__ == '__main__':
    app.run(debug=True)