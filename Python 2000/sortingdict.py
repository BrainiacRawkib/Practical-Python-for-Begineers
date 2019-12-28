def sortlogic(ref):
    return len(ref)


data = {'First': 'John', 'Last': 'Doe', 'Phone': '123-456-789', 'Email': 'foo@bar.net'}

zkeys = list(data.keys())  # a dictionary cannot be sorted that's why the keys are converted to list with the list()
print(zkeys)
zkeys.sort(key=sortlogic)  # it is sorting with the size of the keys. the shortest word comes first and vice versa

# Natural Lookup
for zkey in zkeys:
    print('%10s: [%-20s]' % (zkey, data[zkey]))

zkeys.sort()

# Natural Lookup
for zkey in zkeys:
    print('Sorted %10s: [%-20s]' % (zkey, data[zkey]))
