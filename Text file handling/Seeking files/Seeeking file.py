# Creating variables
fo = 0
# Opening a text file read-binary
fo = open ("ReadThis.txt", "r")
print ("My location : ", fo.tell ())
# Read 10 characters only
print (fo.read (10))
print ("My location : ", fo.tell ())
print (fo.read (3))
print ("My location : ", fo.tell ())
# Seeking to 14th Location (absolute position)
fo. seek (14, 0)
print ("My location : ", fo.tell ())
print (fo.read (4))
print ("My location : ", fo.tell ())
fo. seek (21, 0)
print ("My location : ", fo.tell ())
print (fo.read (2))
print ("My location : ", fo.tell ())
fo. seek (30, 0)
print ("My location : ", fo.tell ())
print (fo.read (4))
print ("My location : ", fo.tell ())
fo. seek (0, 2) # go to end of file
print ("My location : ", fo.tell ())
fo.close ()
