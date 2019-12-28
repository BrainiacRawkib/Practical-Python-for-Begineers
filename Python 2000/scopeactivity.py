dothething = 'Default thang.'


def zapthething():
    """ Demostrate Global """
    # global dothething
    dothething = 'New Thing!'
    print(dothething)


dothething = 'Global'
print('Default : ', dothething)
zapthething()
print('Updated : ', dothething)
