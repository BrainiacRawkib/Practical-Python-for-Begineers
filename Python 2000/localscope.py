def zapthething():
    """ Demonstrate Local """
    dothething = "Local Only"  # local!
    print(dothething)


dothething = 'Global'

print('Default : ', dothething)

zapthething()

print('Not Updated : ', dothething)
