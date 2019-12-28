def showstars(num):
    return '\t' + ("*" * (num + 3))


def show(message):
    xx = len(message)
    stars = showstars(xx)
    print(stars)
    print('\t* ' + message + ' *')
    print(stars)


show('This is a message')
