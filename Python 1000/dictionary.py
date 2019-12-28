ss = 0

prefix = {1: 'DEBUG', 2: 'WARNING', 3: 'ERROR', 4: 'MESSAGE'}

for entry in prefix:
    print(ss, ': ', entry.__hash__())
    ss += 1
