name = input('Enter your name : ')

print('Hello ', name, '!')
while True:
    try:
        age = int(input('What is your age : '))
        print('%s is %d years old.' % (name, age))
    except ValueError:
        print('Sorry, that age is not numeric!')
    else:
        print('\t What else happens?')
        break
    finally:
        print('Data entry completed!')
