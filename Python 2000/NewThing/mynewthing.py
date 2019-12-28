def callafunc():
    """ callafunc: Demonstrate simple importation """
    return "Greetings from callafunc"


print("__doc__ : ", callafunc.__doc__, end='\n\n--=*=--\n\n')
help(callafunc())
print('aka : callafunc():', callafunc())
