class MyClass:
    pass


class YourClass(MyClass):
    pass


foo = MyClass

if type(foo) is type(MyClass):
    print('is a base class!')


if type(YourClass) is type(MyClass):
    print('MyClass is a base class of YourClass!')


if type(foo) is type(YourClass):
    print('is a self, also!')

if type(MyClass) is type(YourClass):
    print('MyClass is Parent Class of YourClass')

if type(YourClass) is type(MyClass):
    print('YourClass is ChildClass of MyClass')
