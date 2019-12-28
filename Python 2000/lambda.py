lamba = lambda x: x * 2

print(lamba(12))

lambb = lambda x, y, z: lamba(x) + (y * 2) + (z * 2)

print(lambb(12, 13, 14))
