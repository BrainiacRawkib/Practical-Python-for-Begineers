def args(*argv):
    print(type(argv))
    count = 0
    for ref in argv:
        print(count, ref)
        count += 1


args('Combine', 'One', 'Two', 'Three')


print('*' * 20)


def args(**argv):
    print(type(argv))
    count = 0
    for ref in argv.values():
        print(count, ref)
        count += 1


args(op='Combine', fi='One', se='Two', th='Three')


print('*' * 20)


def args(**argv):
    print(type(argv))
    count = 0
    for ref in argv.items():
        print(count, ref)
        count += 1


args(op='Combine', fi='One', se='Two', th='Three')
