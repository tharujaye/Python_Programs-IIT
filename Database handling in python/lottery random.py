import random

lotteryNum=[]
userNum=[]

for i in range (5):
    x=random.randrange(1,100)
    lotteryNum.append(x)

for i in range(5):
    l=int(input("Enter your lottery number"))
    userNum.append(l)

print(lotteryNum)
print(userNum)

                
