class MyRep(int):
    def __init__(self):
        print('Constructor')

    def __del__(self):
        print('Deletion')

        # def __new__(self):
        #     print('New')


one = MyRep()
two = MyRep()
del two
