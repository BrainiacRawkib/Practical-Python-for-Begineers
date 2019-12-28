class MyError(Exception):

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return self.value


try:
    pass
    # using
    raise MyError('Tossing it in!')
except Exception as ex:
    print('GOT: ', ex)
else:  # New!
    print('All is well!')
