# this program will show b connection with an error
import mysql.connector
from mysql.connector import Error
# Exception handling
try:
    conn = mysql.connector.connect (host='localhost' ,user='root' ,password='asdfghjkl')
    if conn.is_connected ():
        print ("Conected")
except Error as e:
    print ("Oops!")
    print (e)
