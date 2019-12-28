ss = 0  # initialize ss to 0

while ss != 999:  # test the condition to terminate when ss == 999
    print(bin(ss))  # change the decimal to binary
    print(hex(ss))  # change the decimal to hexadecimal
    print(oct(ss))  # change the decimal to octal
    ss = input('Enter number : ')  # input prompt to enter a new value for ss from the user
    try:
        ss = int(ss)  # cast the input value to integer incase the value entered is not integer(float, character,string)
    except Exception:
        ss = bytearray(ss, 'ascii')  # creating a bytearray of the value entered for ss as an ascii encoding type
        # other encoding values are utf-8, utf-32, utf-16, unicode.
        # the encoding type helps to cover all characters(i.e letters, integers, symbols, etc)
        # therefore ss will be converted according to the ascii encoding type
        ss = int.from_bytes(ss, byteorder='little')  # int.from_bytes converted the bytearray to integer
        # byteorder is also a required argument which has 'big' and 'little' as its values
        # therefore, int.from_bytes(ss, byteorder='little'); ss is the bytearray and byteorder is also required
        # for 'big' format : it has its most significant bit first
        # for 'little' format : it has its least significant bit first

        # intel uses the 'little' format

