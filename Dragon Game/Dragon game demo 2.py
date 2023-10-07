def myfun():
    print("")

    import time
    import random

    user_input=0
    y=0
    n=0
    lp=0

    function=True
    while function:

        
        print("You are in the Kingdom of Dragons")
        time.sleep(1)
        print("In front of you see two cave")
        time.sleep(2)
        print("In one cave, the dragon is friendly and will")
        print("share his treasure with you.")
        time.sleep(1)
        print("The other dragon is hungry and will eat you on sight.")

        time.sleep(1)

        cave=[1,2,3,4,5]
        cave1=random.choice(cave)
        print(cave1)

            
        user_input=int(input("\nCave 1,2,3,4 or 5 : "))


        print("\nYou approach the cave...")
        time.sleep(1)
        print("A large dragon jumps out in front of you!")
        print("He opens his jaws and...")
        print("")
        time.sleep(1)

        if cave1==user_input:
            print("Greets you and then gives you his treasure!")
        else:
            print("Gobless you down")

        print("")
        

        lp=str(input("Do you want to play again (y/n) : "))
        if lp=='n':
            exit()
        else:
            myfun()
            
myfun()
    
