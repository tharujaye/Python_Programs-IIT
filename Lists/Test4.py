MyList=[100,200,550,200,150]
List2=["hi","how","are","you"]

print(MyList)
print(MyList[1:4])
print(len(MyList))

NewList=MyList+List2
print(NewList)

NewList=MyList*2
print(NewList)

print(111 in MyList)

for Value in MyList:
    print(Value)

print(MyList.count(200))

print(MyList)
MyList.reverse()
print(MyList)

MyList.sort()
print(MyList)

MyList.sort(reverse=True)
print(MyList)
