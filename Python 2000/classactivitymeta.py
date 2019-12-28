class MyGreater(int):
    age = 0

    def __init__(self, age):
        self.age = age

    def __gt__(self, comp):
        print('Python Framework calls __gt__(...)!')
        return super.__gt__(self, comp)


comp1 = MyGreater(123)
comp2 = MyGreater(345)
print(comp1 > comp2)


# class member methods

# Public(default)
# Private (_  prefix)
# Mangled Private(__  prefix)

