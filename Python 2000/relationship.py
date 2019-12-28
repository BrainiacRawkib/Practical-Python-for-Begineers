value = None

print(type(value))
if type(value) is type(None):
    print('\nGot de "Null!"')


print('*' * 25)

value = 123
print(type(value))
if type(value) is type(int()):
    print('\tGot de int...')


print('*' * 25)

value = str(123)
print(type(value))
if type(value) is not type(int()):
    print('\tNo got de int!')



