# File: MtListDelta.py

zList = ['Fred', "Ralph", "Zelda", "Zoe"]

# Lists are mutable

print(type(zList))
for ss in range(len(zList)):
    zList[ss] = "Guest " + zList[ss]
    print(zList)
    print(zList[ss])
    print(ss, '\n')
