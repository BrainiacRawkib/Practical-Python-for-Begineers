num = 0x80
val = 0x20

while val <= 256:
    print('%s(%s) ' % (hex(val), chr(val)), end='')
    val += 1
    if val % 8 == 0:
        print()
        continue
    if val >= num:
        break


print('\n\n', '*' * 30, '\n\n')

while val <= 256:
    print('%s(%s) ' % (hex(val), chr(val)), end='')
    val += 1
    if val % 8 == 0:
        print()
        continue
    # if val >= num:
    #     break
