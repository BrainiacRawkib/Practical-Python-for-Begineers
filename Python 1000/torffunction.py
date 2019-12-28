def readinput():
    zoption = input('Input:')
    return zoption.isalnum()


torf = readinput()


if torf == True:
    print('is not special')
else:
    print('is special')
