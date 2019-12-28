def subset(arg):
    # Yield = Add expression to result
    for a in arg:
        if a % 2 == 0:
            yield a


items = [n for n in range(1, 100)]  # list comprehension

copy = list(subset(items))

print('Subset: ', copy)

copy = tuple(subset(items))

print('Subset: ', copy)

