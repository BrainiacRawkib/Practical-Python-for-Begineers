# my solution

# i = 1
#
# while i != 100:
#     print(i, end=' ')
#     if i % 10 == 0:
#         print()
#     if i > 90:
#         print('...')
#         break
#     i += 1

#  instructor solution


start = 10
stop = 90
total = 0

while True:  # Loop Forever!
    print(start, end=' ')
    total += 1
    start += 1
    if total % 10 == 0:
        print()
        continue
    if start >= stop:
        break
print('...')
