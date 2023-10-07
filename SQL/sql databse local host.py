import mysql.connector

#Estabiish a connection to the MysQL server
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password=""
)

#Create a new database named "ab_test _python"
mycursor=mydb.cursor()
mycursor.execute("CREATE DATABASE dpython")

#Connect to che new database
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="dpython"
)
#Create a new table named "tbl mytable"
mycursor=mydb.cursor()
mycursor.execute ("CREATE TABLE tbl_mytable (No INT, FName VARCHAR(15), City VARCHAR(15))")
