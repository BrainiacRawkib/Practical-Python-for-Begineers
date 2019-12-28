class MyConMgr():
    zname = 'init.name'

    def __enter__(self):
        pass

    def __exit__(self, xtype, xval, trace):
        pass

    def name(self):
        return self.zname


bla = MyConMgr()

with bla:
    print('with:\t', bla.name())  # enter block
print('xblock:\t', bla.name())  # exit block
