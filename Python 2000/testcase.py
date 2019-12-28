class Test(object):
    test = None

    def gettest(self):
        self.test = 'self.test'
        test = 'Tested'
        return test

    def selftest(self):
        return self.test

    def getnewtest(self):
        test = 'getnewtest'
        return test

    def getnotest(self):
        test = 'getnotest'
        return test


tested = Test()
print('Local Result tested.gettest() : ', tested.gettest())
print('Local Result tested.selftest() : ', tested.selftest())
print('Local Result tested.getnewtest() : ', tested.getnewtest())
print('Local Result tested.getnotest() : ', tested.getnotest())

