print('First: %d, Second: %d' % (42, 22))  # % method
print('First: {0}, Second: {1}'.format(42, 22))  # .format method
print('First: {}, Second: {}'.format(22.42, 22))
print('Second: {1}, First: {0}'.format(42, 22))


print('First: {foo}, Second: {bar}'.format(foo='Mr. Foo', bar='is bar'))
print('Second: {bar}, First: {foo}'.format(foo='Mr. Foo', bar='is bar'))
print('First: {foo}, Second: {bar}, Third: {rab}'.format(foo='Mr. Foo', bar='is bar', rab='rab'))


print('Name: [{0:<12s}], Age: {1:12d}, Balance: ${2:07.2f}, Last Name: [{3:12s}]'.format('Client', 64, 22.42, 'Unknown'))
print('Name: [{0:>12s}], Age: {1:<12d}, Balance: ${2:<07.2f}, Last Name: [{3:>12s}]'.format('Client', 64, 22.42, 'Unknown'))

# 0:, 1:, 2: and 3: represent the index of the format values('Client', 64, 22.42, 'Unknown')
# 12s reps the number of whitespace to the right and it's also left justified. it is also same as <12s
# >12s reps the number of whitespace to the left and it's also right justified. it is also same as >12s
# this above practice with whitespace can also be done with zero (0)


# Used more than one i.e using one format value in many format index

print("More: {0:6.2f} or  {0:6.3f}".format(5.1234))


# One format value can be used if many are supplied

# Extra parameters ignored.
print('More: {0:6.2f} or {0:6.3f}'.format(12.345, 5.1234))
print('More: {1:6.2f} or {1:6.3f}'.format(12.345, 5.1234))


