class MyData(object):
    age = 0
    name = ''

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def readdata(self):
        self.name = input('Enter Your Name : ')

        while True:
            try:
                self.age = int(input('What is your age : '))
                break
            except ValueError:
                print('Sorry, the age is not numeric!')


info = MyData('Nagy', 23)
# info.readdata()
print(info.name, 'is ', info.age)
