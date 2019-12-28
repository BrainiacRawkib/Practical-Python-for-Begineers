value = None

print(type(value))
if type(value) is type(None):
    print('\tGot de Null...')


value = 123

print(type(value))
if type(value) is type(int()):
    print('\tGot the int...')


value =str(123)

print(type(value))
if type(value) is type(str()):
    print('\tGot the str...')


