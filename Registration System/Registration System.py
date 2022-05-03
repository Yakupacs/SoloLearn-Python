try:
    name = input()
    if 3 < len(name):
        print("Account Created")
    else:
        raise Exception
    #your code goes here
except:
    print("Invalid Name")