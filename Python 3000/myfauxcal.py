
# zlist = [n for n in range(1, 32) if n % 7 == 0]
#
# print(zlist)

zfile = open('myfauxcal.txt', 'w')

for day in range(1, 32):
    print('%3d' % day, end=" ")  # print to the screen (console)
    print('%3d' % day, end='', file=zfile)  # print to the file (myfauxcal.txt)
    if day % 7 == 0:
        print()  # the results are displayed in the interval of 7s in new line
        print(file=zfile)  # the results are displayed in the interval of 7s in new line into the myfauxcal.txt file

zfile.close()
