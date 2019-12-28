data = []

data.append('John Doe, 12345 Fifth Ave., 813-318-9999')
data.append('Mr. Goober, 8712 Main Street, 425-514-9999')
data.append('Prof. Nagy, 105 Baker Street, 742-427-9999')
data.append('Doctor Quote, 666 Social Security Lane, 781-187-9999')

ss = 0

for line in data:
    fields = line.split(',')
    print('fields : ', fields)
    print('Length of data : ', len(data))
    print('Length of fields : ', len(fields))  # Length of each info that are appended not length of variable 'data'
    if len(fields) != 3:
        print('Field Error!')
    else:
        ss = ss + 1
        print('\n', str(ss) + ": " + fields[0])
        print(str(ss) + ": " + fields[1])
        print(str(ss) + ": " + fields[2], '\n')

