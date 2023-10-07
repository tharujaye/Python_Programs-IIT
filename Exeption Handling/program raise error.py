marks = 0
try:
    marks = int (input ("Type term test marks : "))
    if marks<0 or marks>100:
        raise Exception ("Value must be in the range of 0 to 100")
    else:
        print ("Marks with in the range")
except ValueError:
    print ("Not a value")
except Exception:
    print ("Marks not in range")
else:
    print ("Program worked successfully")
