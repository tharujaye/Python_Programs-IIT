#initiating variables
marks=0
student=0

studentList=[]
marksList=[]
    
def myFun():
    
    #getting user inputs

    student=input("Type student name : ").capitalize()
    studentList.append(student)
    marks=int(input("Type student mark : "))
    marksList.append(marks)
    return

for i in range(5):
    myFun()
    
#giving stars system
for i in range(5): 
    print(studentList[i]," \t\t : ",marksList[i] , "% \t>>  " , "*"* (marksList[i]//10))

#Total marks expression
totalMarks=sum(marksList)
print("Total marks of the whole class : ",totalMarks)

#average marks expression
averageMarks=totalMarks/(len(studentList))
print("Average marks of the whole class : ",averageMarks)
    

