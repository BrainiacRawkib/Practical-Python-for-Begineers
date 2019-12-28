class MyData(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def InputData():  # no self parameter
        result = MyData('Que', -1)
        result.name = input('Enter Your Name : ')
        while True:
            try:
                result.age = int(input('What is your age : '))
                break
            except ValueError:
                print('Sorry, the age is not numeric!')
            finally:
                print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        return result


info = MyData.InputData()
print(info.name, 'is ', info.age)
