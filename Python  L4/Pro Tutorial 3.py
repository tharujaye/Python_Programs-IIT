#P1
#a)
n = int(input('Give me a number over 100: '))
if n <= 100:
    print(n, 'is not over 100')

else :
    print(n, 'is less than 100')


#b)
age=int(input('Enter your age: '))
if age>=18:
    print("can vote")
else:
    print("can't vote")

#P2
#a)
x = int(input('Give me a number: '))
if x < 0:
    print(x, 'is negative')
else:
    print(x, 'is positive')

#b)
marks=int(input("Enter your marks: "))
if marks<40:
    print ("Fail")
else :
    print ("Pass")


#c)
num=int(input("Enter a number: "))
if num%1:
    print("This is an odd number")
else:
    print("This is an even number")


#P3
#a)

option=int(input("Enter 1’ if want to convert from Celsius to Fahrenheit or Enter 2' if want to convert from Fahrenheit to Celsius"))
if option==1:
    c=int(input("Enter temperature in 'C: "))
    f = (c * 1.8) + 32
    print(f)

else:
    f=int(input("Enter temperature in 'F: "))
    c = (f - 32) / 1.8
    print(c)

#b)
value=int(input("Enter a value: ")
          

