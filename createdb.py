# Execute this only one time to create a fingerprint database
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE fingerdb")

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database='fingerdb'
)
mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE fingers (finger VARCHAR(255), userid VARCHAR(255))")
