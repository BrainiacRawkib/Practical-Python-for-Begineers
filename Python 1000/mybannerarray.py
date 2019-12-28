prefix = ['DEBUG', 'WARNING', 'ERROR', 'MESSAGE']


def showchars(num, token):
    return '\t' + (token * (num + 4))


def show(ss, message):
    if ss < 1:
        ss = 1
    if ss > len(prefix):
        ss = len(prefix)
    message = prefix[ss - 1] + ': ' + message
    xx = len(message)
    stars = showchars(xx, '*')
    print(stars)
    print('\t' + message + ' *')
    print(stars)


# def Append(zpre):
#     prefix.append(zpre)
#
#
# Append('TEST')
show(999, 'This is a test')
show(4, 'This is a message')
show(3, 'This is a error')
show(2, 'This is a warning')
show(1, "Doh!")

for dat in prefix:
    print(dat)

# app = ['CRITICAL', 'CONDITION']
# Append(app)
#
# for ss in range(len(prefix)):
#     print(ss, ': ', prefix[ss])
