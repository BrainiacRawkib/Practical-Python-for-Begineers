class Foo():

    zname = 'init.name'

    def __enter__(self):  # with block
        self.zname = 'with.enter.name'

    def __exit__(self, xtype, xval, trace):
        self.zname = 'with.exit.name'

    def name(self):
        return self.zname


# Just an object
bla = Foo()


# Consistent block entry / exit values

print('pre:\t', bla.name())  # True

if True:
    print('block:\t', bla.name())  # normal

# Activate __enter__ via 'with'

try:
    with bla:
        print('with:\t', bla.name())  # enter block
    print('xblock:\t', bla.name())  # exit block
finally:
    print('finally:', bla.name())  # exit block

print('post:\t', bla.name(), 'still!')

