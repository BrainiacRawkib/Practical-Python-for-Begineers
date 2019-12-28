data = {'First': 'John', 'Last': 'Doe', 'Phone': '123-456-7890'}


byval = data['Phone']
byref = id(data['Phone'])  # still a copy

print(byval)

print(byref)

data = {'First': 'John', 'Last': 'Doe', 'Phone': '321-654-0987'}

byval = data['Phone']
byref = id(data['Phone'])  # still a copy

print(byval)

print(byref)
