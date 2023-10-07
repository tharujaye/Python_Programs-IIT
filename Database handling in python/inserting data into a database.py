import mysql.connector

# Open database connection with a dictionery

conDict = {'host': 'localhost',
'database': 'tharu',
'user':'root',
'password':'asdfghjkl'}

db = mysql.connector.connect(**conDict)

# prepare a cursor object using cursor () method
cursor = db.cursor ()

# execute SQL query using execute () method.
myInsertText = "INSERT INTO tb1 mytable VALUES (5, 'Judi', 'Zilva', 'Rathmalana')"
cursor.execute(myInsertText)

# Commit the change
db.commit()
print(cursor.rowcount, "Record Added")

# disconnect from server
db.close()
