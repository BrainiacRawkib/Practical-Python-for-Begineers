def bigsky():
    global ThisString
    ThisString = 'Default'


def Remote():
    ThisString = 'Hello Remote'
    print(ThisString)


bigsky()
print(ThisString)
ThisString = 'Spam!'
Remote()
print(ThisString)