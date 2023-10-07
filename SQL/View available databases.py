import mysql.connector

# Open database connection
db = mysql.connector.connect (host="localhost",user="root",password="asdfghjkl")

# prepare a cursor object using cursor () method
cursor = db.cursor()

# execute SQL query using execute () method.
cursor.execute (" SHOW DATABASES")

# Fetch results using fetchall () method.
data = cursor. fetchall ()
print ("Available databases : %s " % data)

# disconnect from server
db.close()
