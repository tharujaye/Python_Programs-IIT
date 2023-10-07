fo=0

fo=open("TextFile.txt","r")
#with fo :
count=0
for line in fo:
    #Reading line by line
    count+=1
print(count,"Lines in the text")
fo.close()
    
