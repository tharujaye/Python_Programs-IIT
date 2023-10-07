try:
    print(value)
except NameError:
    print("Name error was captured")
except:
    print("General capture")
