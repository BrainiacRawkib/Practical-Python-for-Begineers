def decoder(arr):
    alphabets = 'abcdefghijklmnopqrstuvwxyz'
    output = ''
    for i in arr:
        output += alphabets[i]

    return output


item = [x for x in range(1, 20)]
test = decoder(item)
print(test)
