import csv

for zlang in csv.list_dialects():
    print('csv Dialect: ', zlang)


zdata = ('Naggy', 12345, 'How to, Python', 14.95)


# File Write

zfile = open('book.csv', 'w')
writer = csv.writer(zfile, dialect='excel')
writer.writerow(zdata)

zfile.close()


# File Read


zfile = open('book.csv', 'r')
reader = csv.reader(zfile, dialect='excel')
for line in reader:
    if len(line) != 0:
        print('Read: ', line)

zfile.close()
