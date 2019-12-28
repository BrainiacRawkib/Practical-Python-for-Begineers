prefix = set()
prefix.add('Pig')
prefix.add('Sheep')
prefix.add('Goat')
prefix.add('Cow')
prefix.add('Bull')
prefix.add('Dog')
prefix.add('Cat')

print(prefix)

prefix2 = set(("Ant", "Mouse", "Pig", 'Bull'))

print('Intersection : ', prefix2.intersection(prefix))
print('Union : ', prefix2.union(prefix))

superset = prefix2.union(prefix)

print('Superset : ', prefix2.issubset(superset))

print('Subset : ', superset.issuperset(prefix))

cat = {'c', 'a', 't'}
car = set()
car.add('c'); car.add('a'); car.add('r')

print('cat : ', cat)

print('car : ', car)


