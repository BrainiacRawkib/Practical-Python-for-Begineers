zchars = 'TheTest'

print('ascii : ', bytes(zchars, 'ascii'))
print('utf8 : ', bytes(zchars, 'utf8'))
print('utf16 : ', bytes(zchars, 'utf16'))
print('utf32 : ', bytes(zchars, 'utf32'))
print('ascii : ', bytearray(zchars, 'ascii'))
print('utf8 : ', bytearray(zchars, 'utf8'))
print('utf16 : ', bytearray(zchars, 'utf16'))
print('utf32 : ', bytearray(zchars, 'utf32'))
