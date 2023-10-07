import mysql.connector

# Establish a connection to the MySQL server
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password=""
)

# Create a new database named "db_test_python"
mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE suu")

# Connect to the new database
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="suu"
)

# Create a new table named "tbl_mytable"
mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE tbl_mytable (No INT, FName VARCHAR(15), MName VARCHAR(15), City VARCHAR(15))")

