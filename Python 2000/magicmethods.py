import copy
x = 2
y = 3

print(x.__gt__(y))

print(x.__hash__())

print(x.__str__())

print(x.__repr__())

a = copy.copy(x)

print('copy a from x : ', a)
