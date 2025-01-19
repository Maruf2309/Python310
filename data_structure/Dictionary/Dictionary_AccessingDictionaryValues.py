## ---> Example 2: Accessing Dictionary Values

my_dict = {'name':'Piter','age':35, 'city':'Canada', 'gender':'Male'}

# Values in a dictionary are accessed using their keys.
# If a key is not found, a KeyError will be raised unless you use the get() method, which returns None.
# Accessing values using keys
name = my_dict['name']
city = my_dict['city']
gender = my_dict['gender']

#Printing accessed values
print('Name:',name)
print('City:',city)
print('Gender:',gender)