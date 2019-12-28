def showchars(num, token):
    return '\t{}'.format(token * (num + 4))


def show(message):
    stars = showchars(len(message), '*')
    print(stars)
    print('\t**{0:%<s}**'.format(message))
    print(stars)


show('  SPECIAL  ')
show('  SALE  ')
show('SALE')
