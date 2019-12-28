zdata = ('Nagy', 12345, 'How to Python', 14.95)

zfile = open('book.txt', 'w')

print('"', zdata[2], zdata[1], zdata[0], zdata[3], '"', sep=' - ', file=zfile)

zfile.close()

zfile = open('book.txt', 'r')

zdata = zfile.readline().split('-')
print(zdata)

zfile.close()
