for val in range(0x20, 0x80):
    print('%s(%s)' % (hex(val), chr(val)), end='  ')
    if val % 3 == 0:
        print()

