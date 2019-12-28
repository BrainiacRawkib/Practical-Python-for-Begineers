# Combination Factorial Code

from math import factorial

n = int(input('Enter the value of n : '))
r = int(input('Enter the value of r : '))

if r > n:
    print('\nMath Error. r is supposed to be less than n')
else:
    x = factorial(n) / (factorial(n - r) * factorial(r))
    print('\nThe result of the factorial is : ', x)

