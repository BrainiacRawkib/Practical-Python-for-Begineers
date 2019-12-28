data = bytes([1, 2, 3, 4])  # bytes are immutable
print(data)
print(data[2])

data = bytearray([1, 2, 3, 4, 5])  # bytearray are mutable
data.append(42)
print(data)
