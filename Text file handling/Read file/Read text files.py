#creating variables
fo=0

#you have to have a file called
#MyText.txt with some text in the same file

#Open a text file with
fo=open("MyText.txt", "r")
print("File name : ",fo.name)
print("Which mode? : ",fo.mode)
print("What is in it?\n===============MyTextSub2.txt================")
print(fo.read())

# Accessing files in sub folder
fo2=open("Sub/MyTextSub2.txt", "r")
print("what is in it?\n=================")
print(fo2.read ())
