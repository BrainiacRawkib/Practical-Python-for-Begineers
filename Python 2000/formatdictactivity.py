data = {'Email': 'foo@bar.net', 'Phone': '123-456-789', 'Last': 'Doe', 'First': 'John'}

zkeys = data.keys()

# Natural lookup
# for zkey in zkeys:
#     print(zkey)
#     print('%10s:[%-20s]' % (zkey, data[zkey]))
#
#     # Member lookup
#     for zkey in zkeys:
#         print('%10s:[%-20s]' % (zkey, data.get(zkey)))
for ss in data:
    # print('key : ', ss)
    # print('value : ', data[ss])
    print('%10s: [%-20s]' % (ss, data[ss]))
