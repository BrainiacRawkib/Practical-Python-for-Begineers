def oddoreven(max):
    for item in range(max):
        if item % 2 == 0:
            yield 'even', item
        else:
            yield 'odd', item


maxnum = list(oddoreven(100))

print(maxnum)

maxnum = tuple(oddoreven(100))

print(maxnum)


for name, num in oddoreven(7):  # name reps 'even' or 'odd' , num reps item
    print('{} is surely {}!'.format(num, name))


print('*' * 30)


hel = 'string and integer'

for n, m in enumerate(hel):
    print('{} is {}!'.format(n, m))
