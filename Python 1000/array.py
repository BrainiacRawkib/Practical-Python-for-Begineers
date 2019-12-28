import array

data = array.array('b')
print(data)

data.append(2)
print(data)
data.append(3)
print(data)

# data.append('g')  # array does not append string and float just integer only
# data.append(3.22)  # array does not append string and float just integer only


zbytes = b'123'
data.append(zbytes[0])
data.append(zbytes[1])
data.append(zbytes[2])
# data.append(zbytes[3])  # it will throw an error because it's not in b'123'
print(data)
data.append(b'ABC'[0])
print(data)

data = array.array("b", b"Bizinga")
print(data)
