option = input('Press any key, then tap "enter":')

torf = option.isalnum()

if torf == True:
    print(option, 'is not special')
else:
    print(option, 'is special')
