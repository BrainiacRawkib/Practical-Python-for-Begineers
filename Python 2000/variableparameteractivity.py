def args(*argv):  # tuple
    print(type(argv))
    count = 0
    for ref in argv:
        print(count, ref)
        count += 1


args('Combine', 'First')


print('*' * 30)


def args(**argv):  # dictionary
    print(type(argv))
    count = 0
    for ref in argv.values():
        print(count, ref)
        count += 1


args(op='Combine', fi='First')


print('*' * 30)


def args(**argv):  # dictionary
    print(type(argv))
    count = 0
    for ref in argv.items():
        print(count, ref)
        count += 1


args(op='Combine', fi='First')


print('*' * 30)


def args(**argv):  # dictionary
    print(type(argv))
    count = 0
    for ref in argv:
        print(count, ref)
        count += 1


args(op='Combine', fi='First')


print('*' * 30)


def args(argv):  # string or integer depending on the parameter passed
    print(type(argv))
    count = 0
    for ref in argv:
        print(count, ref)
        count += 1


args(['combine'])


print('*' * 30)


def args(argv):  # string
    print(type(argv))
    count = 0
    for ref in argv:
        print(count, ref)
        count += 1


args('combine')

# this function cannot accept integer because the function is for iterable data types
