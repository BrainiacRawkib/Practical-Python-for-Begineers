num = 321

print('Numeric Views')
print('As Decimal: ', num)
print('As Hex: ', hex(num))
print('As Octal: ', oct(num))
print('As Binary: ', bin(num))
print('\n~~~~~~~~~~~~~~ ')
# print('As Reversed Decimal: ', num[::-1])  # int object is not subscriptable i.e it is not reversible with [::-1]
# print('As Reversed Decimal: ', reversed(num))  # int object is not reversible i.e int cannot be reversible
print('\nReversed Numeric Views')
print('As Reversed Hex: ', hex(num)[::-1])  # hexadecimal value are reversible
print('As Reversed Octal: ', oct(num)[::-1])  # octal value are reversible
print('As Reversed Binary: ', bin(num)[::-1])  # binary value are reversible


value = 0xA

print('\n Strings Views')
print('As Decimal: ', value)
print('As Hex: ', hex(value))  # hexadecimal value are reversible
print('As Octal: ', oct(value))  # octal value are reversible
print('As Binary: ', bin(value))
print('\n~~~~~~~~~~~~~~ ')


print('\nReversed Strings Views')
# print('As Decimal: ', value)  # decimal cannot be reversed
print('As Reversed Hex: ', hex(value)[::-1])  # hexadecimal value are reversible
print('As Reversed Octal: ', oct(value)[::-1])  # octal value are reversible
print('As Reversed Binary: ', bin(value)[::-1])

