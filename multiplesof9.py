n = 9

# while n != 250:
#     arr = []
#     if n % 9 == 0:
#         total = 0
#         total += n  # total.__add__(n) also do the same as total += n but just that you've to equate to a variable
#         arr = total
#         print(arr)
#     n += 1

# for n in range(9, 250):
#     total = 0
#     if n % 9 == 0:
#         total += n
#         print(total)


def multiples(arg):
    # Yield = Add expression to result
    for a in arg:
        if a % 9 == 0:
            yield a


items = [n for n in range(9, 250)]  # list comprehension

multiple = list(multiples(items))

print('multiples: ', multiple)
print('Sum: ', sum(multiple))


# Solution Two


def sum_of_multiples(a):
    a = [x for x in range(9, 250) if x % 9 == 0]
    s = 0
    for x in a:
        s += x

    print(s)


sum_of_multiples(range(9, 250))

