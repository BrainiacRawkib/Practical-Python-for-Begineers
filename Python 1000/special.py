""" Example to demonstrate requirement mapping"""
# Get as str() from the user
option = input('Press any key, then tap "enter":')

# Use associated "member function" of str()
if option.isalnum():
    # If is alpha-numeric
    print('is not special')
else:
    # If is NOT alpha-numeric
    print('is special')

# Show what was entered
print("option='" + option + "'")

