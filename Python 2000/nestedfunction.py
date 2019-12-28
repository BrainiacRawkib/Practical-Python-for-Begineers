def func():
    value = 1

    def calc():
        # How to re-use above?
        nonlocal value  # nonlocal make the local variable nonlocal only in the parent(s) function but cannot be used outside the parent(s) function
        value = 2
        print('calc value : ', value)
    calc()
    print('func value : ', value)


func()
# print(value)
