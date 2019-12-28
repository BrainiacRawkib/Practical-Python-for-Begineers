value = None

print(type(value))


print('*' * 15, 'Class Func', '*' * 15)


class Func(object):
    value = None
    print('value in the class(outside the methods): ', value)

    def calc(self):
        self.value = 20
        value = 2
        return value  # it will return the value of 2 because we set value = 2 in this method

    def getvalue(self):
        return self.value  # it will return the value of 20 in calc() because it returns self.value and not value alone

    def getnone(self):
        return value  # it will return the value of None because we set value to None outside the methods,
        # but in the class

    def getnewvalue(self):
        value = 8
        return value

    def getvalue(self):  # if two methods are found in one class the later value overrides the earlier value if returned
        # value = 14  # this value = 14 in this method will override the first getvalue() method declared earlier
        return value  # but this method will return None because it is value and not self.value


foo = Func()
print('Local Result foo.calc() : ', foo.calc())
print('Class Result foo.getvalue()  : ', foo.getvalue())
print('Class Result foo.getnone()  : ', foo.getnone())
print('Class Result foo.getnewvalue()  : ', foo.getnewvalue())
print('Class Result Second foo.value()  : ', foo.getvalue())


print('\n', '*' * 15, 'Assert', '*' * 15, '\n')


foo = Func()


assert(foo.value is None)
print('Local Result : ', foo.calc())
print('Class Result : ', foo.getnewvalue())
assert (foo.value is not None)

