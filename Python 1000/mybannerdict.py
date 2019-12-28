prefix = {1: 'ERROR', 2: 'DEBUG', 3: 'WARNING', 4: 'MESSAGE'}


def showchars(num, token):
    return '\t' + (token * (num + 4))


def show(ss, message):
    if ss < 1:
        ss = 1
    if ss > len(prefix):
        ss = len(prefix)
    message = prefix[ss] + ': ' + message  # dictionary prefix[ss] is not like list prefix[ss - 1] because dict uses the index number as the keys for the dictionary.
    xx = len(message)
    stars = showchars(xx, '*')
    print(stars)
    print('\t' + message + ' *')
    print(stars)


show(12, 'This is any')
show(3, 'This is any')
