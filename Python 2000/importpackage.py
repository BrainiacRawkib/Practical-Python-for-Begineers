# Package Qualification Required
import collections

bog = collections.OrderedDict(foo='bar', foo2='net')
print(type(bog))
print(bog)

# Add to "Local Namespace"
from collections import OrderedDict
bog = OrderedDict(foo="bar", foo2='net')
print(type(bog))
print(bog)

import sys
print(sys.path)

for ref in sys.path:
    print(ref)

for zindex, znode in enumerate(sys.modules):
    print(zindex + 1, znode)
