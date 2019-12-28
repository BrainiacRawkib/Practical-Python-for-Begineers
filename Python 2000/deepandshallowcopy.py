#  file


def dumper(theme, zlist):
    print(theme)
    for ref in zlist:
        print('\tAddress: ', hex(id(ref)), '\t{}'.format(ref))
    print('Collection : ', hex(id(zlist)))


zdata = ['one', 'two', 'three']

# zdata = ['Big', 'Bad', 'Bit']

dumper('original', zdata)

cpdeep = list(zdata)
dumper('Deep-copy', cpdeep)

cpshallow = zdata
dumper('Shallow-copy', cpshallow)

# Deep-copy does not change the memory address but shallow-copy does
# Deep-copy can be done by using the data type method to cast that particular type of data

zdata[0] = 'big'
zdata[1] = 'bad'
zdata[2] = 'bit'

dumper('original', zdata)

cpdeep = list(zdata)
dumper('Deep-copy', cpdeep)

cpshallow = zdata
dumper('Shallow-copy', cpshallow)

