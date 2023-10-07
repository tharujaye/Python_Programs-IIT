Set1 = {1,2,3,4}
Set2 = {10,20,30,40}

print(Set1)
print(Set2)

New = Set1.union(Set2)
print(New)

del Set2

print(Set1)

MyTuple = (10,20,30,40)
print(MyTuple)
print(len(MyTuple))
print(MyTuple*2)
print(30 in MyTuple)
for Value in MyTuple:
    print (Value)

MyList = [100,200,300,400]

MyTuple_new = tuple(MyList)
print(MyTuple_new)

MyTuple = ("Oh","My","God","Python","Getting","difficult")
MyList_new = list(MyTuple)
print(MyList_new)

MyList_new[2]="Jesus"
print(MyList_new)
