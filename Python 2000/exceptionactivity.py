import sys


try:
    file = open('myfile.txt')
    line = file.readline()
    ival = int(line.strip())

except IOError as ex:
    # How to test a "file not found" error?
    print("IOError({0}) : {1}".format(ex.errno, ex.strerror))  # {0} and {1} are for ex.errno and ex.strerror formats respectively

except ValueError:
    # How to test the integer conversion error?
    print("Unable to convert line to integer.")

except:
    # How to test the catch-all error?
    print("Unexpected exception : ", sys.exc_info()[0])
