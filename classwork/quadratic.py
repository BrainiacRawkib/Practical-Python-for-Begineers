# Quadratic Equation Program

from math import sqrt, pow

a = int(input('Enter the coefficient of a :'))
b = int(input('Enter the coefficient of b :'))
c = int(input('Enter the coefficient of c :'))


d = (pow(b, 2) - (4 * a * c))

if d > 0:
    x1 = (-b + sqrt(d)) / (2 * a)
    x2 = (-b - sqrt(d)) / (2 * a)
    print("\nThe roots are : ", x1, x2)
elif d == 0:
    x = (-b) / (2 * a)
    print("\nThe root is : ", x)
else:
    print('\nThis is a negative root')

