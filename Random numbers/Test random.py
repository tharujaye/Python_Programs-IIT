import random

#Creating variables
rand=0

#generate numbers till 10
rand=random.randrange(10)
print(rand)

#Generate numbers from 1 to 50
rand=random.randrange(1,50)
print(rand)

#Shuffle values in a list
numbers=[1,2,3,4,5,6,7,8,9,10]
print(numbers)
random.shuffle(numbers)
print(numbers)

#Generate next random floating point 0.0 ~ 1.0
rand=random.random()
print(rand)
