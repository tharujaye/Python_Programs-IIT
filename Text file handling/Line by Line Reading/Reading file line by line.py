#Creating variables
fo=0

#Open  a text  file with
fo=open("MyTextLines.txt","r")
with fo :
    count=1
    for line in fo:
        #Reading line by line
        print("Line",count,"-",line,end="")
        count+=1
