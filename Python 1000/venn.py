cat = {'c', 'a', 't'}

car = {'c', 'a', 'r'}

print("Normalized cat : ", cat)
print("Normalized car : ", car)


# set() = unique set, 'venn style

print('cat | car : ', cat | car)  # union
print('cat & car : ', cat & car)  # intersection
print('cat - car : ', cat - car)  # remove common car from cat
print('car - cat : ', car - cat)  # remove common car from cat
print('cat ^ car : ', cat ^ car)  # order differentiation
