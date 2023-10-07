friends = ['Smith', 'Jane', 'Nazeem', 'Judi', 'Don']
try:
    number = int (input ("Type a number to find your friend : "))
    print ("Your friend is :",friends [number])
except IndexError:
    print ("No such friend name under that number")
else:
    print ("Friend found")
