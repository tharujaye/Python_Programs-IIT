import time
import random

print("You are in the Kingdom of Dragons")
time.sleep(1)
print("In front of you see two cave")
time.sleep(2)
print("In one cave, the dragon is friendly and will")
print("share his treasure with you.")
time.sleep(1)
print("The other dragon is hungry and will eat you on sight.")

time.sleep(1)
user_input=int(input("\nCave 1 or 2 : "))
cave=random.randint(1,2)

print("\nYou approach the cave...")
print("A large dragon jumps out in front of you!")
print("He opens his jaws and...")

if cave==1:
    print("Greets you and then gives you his treasure!")
else:
    print("Gobless you down")


