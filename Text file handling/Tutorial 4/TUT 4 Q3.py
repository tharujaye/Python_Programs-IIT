# Creating a variable
fo = 0
num=count=0

# Opening a text file
fo =open ("NumbersList.txt", "r")

fo.seek(0,2) #EOF
size=fo.tell()
fo.seek(0,0)#BOF

#Display the numbers
print ("Numbers", end="")
for line in fo:
    print(line)

fo.seek(0,0)
print("Even Numbers -",end=" ")
while(count<=(size-2)):
    num=int(fo.read(3))
    if(num%2==0):
        print(num,end=" ")
    count+=3

fo.close()
