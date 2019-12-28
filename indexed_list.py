input_file = 'list.csv'

x = []

with open(input_file, 'r') as f:
    for line in f.readlines():
        data = line[:-1].split(', ')
        print 'data ---> ', data
        x.append([data[0]] + data[2:])
print x
