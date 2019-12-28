def mkstring(num, token):
    return '{}'.format(token * num)


def show(message):
    stars = mkstring(20, '*')
    print(stars.center(20))
    print(message.center(20))
    print(stars.center(20))


show(' special ')
show(' sale ')
