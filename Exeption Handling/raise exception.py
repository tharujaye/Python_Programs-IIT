try:
    uni = input ("Type your university : ")
    if uni.upper() != "IIT":
        raise Exception ("OMG You don't know the university?")
    else:
        print ("Very Good")
except:
    print ("Kick this guy out")
