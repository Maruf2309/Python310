'''
Tasks:
1. Creating a Dictionary
2. Accessing Dictionary Values
3. Modifying Dictionary Values
4. Adding Key-Value Pairs to a Dictionary
5. Removing Key-Value Pairs from a Dictionary
6. Dictionary Keys, Values, and Items
7. Checking Membership in a Dictionary
8. Iterating Over a Dictionary
9. Merging Dictionaries
10.Dictionary Length

'''


## ---> Example 1: Creating a Dictionary
# A dictionary is a collection of key-value pairs, created using curly braces {}.
# Each key is unique, and it is used to access its corresponding value.

my_dict = {'name':'Piter','age':35, 'city':'Canada', 'gender':'Male'}

# Priting the created dictionary
# print("Created Dictionary :", my_dict)

## ---> Example 2: Accessing Dictionary Values

# Values in a dictionary are accessed using their keys.
# If a key is not found, a KeyError will be raised unless you use the get() method, which returns None.
# Accessing values using keys
name = my_dict['name']
city = my_dict['city']
gender = my_dict['gender']

#Printing accessed values
#print('Name:',name)
#print('City:',city)
#print('Gender:',gender)

## --->Example 3: Modifying Dictionary Values
# Dictionaries are mutable, meaning their values can be changed by assigning a new value to a key.

# Example dictionary
my_dict = {'name':'John','age':30, 'city':'USA', 'gender':'Male'}

# Modifying a value
my_dict['age'] = 20

# Printing the modified dictionary
# print('Modified Dictionary:', my_dict)


# Example 4: Adding Key-Value Pairs to a Dictionary
# You can add new key-value pairs to a dictionary by assigning a value to a new key.
# Example dictionary
my_dict = {'name':'John','age':30, 'city':'USA', 'gender':'Male'}

# Adding a new key-value pair
my_dict['language'] = 'English'

# Print the updated dictionary
# print(my_dict)



## ---> Example 5: Removing Key-Value Pairs from a Dictionary
# You can remove key-value pairs using the pop() method, which removes the specified key and returns its value.
# The del keyword can also be used to remove a specific key or clear() to remove all items.

# Example dictionary
my_dict = {'name': 'John', 'age': 25, 'city': 'New York'}

# Remove a key-value pair
age = my_dict.pop('age')

# Priting after removal
#print('Dictionary after Removal:', my_dict)
#print('Removed Age:', age)

# Example 6: Dictionary Keys, Values, and Items
# You can retrieve all keys, values, or key-value pairs using the keys(), values(), and items() methods, respectively.

# Example dictionary
my_dict = {'name': 'John', 'age': 25, 'city': 'New York'}

# Retrieving keys, values, and items
keys = my_dict.keys()
values = my_dict.values()
items = my_dict.items()

# Printing keys, values, and items
#print('Keys:',keys)
#print('Values:', values)
#print('Items:',items)

# Example 7: Checking Membership in a Dictionary
# You can use the 'in' keyword to check if a key exists in a dictionary.
# Example dictionary
my_dict = {'name': 'John', 'age': 25}

# 7.1 Checking for membership
if 'name' in my_dict:
    print('Key "name" exists in the Dictionary')
else:
    print('Key "name" not found in the dictionary ')

# 7.2 Checking for membership
if 'city' in my_dict:
    print('key "city" exists in the dictionary')
else:
    print('key "city" not exits in the dictionary, try other!')

# Example 8: Iterating Over a Dictionary
# You can iterate over a dictionary to access its keys, values, or key-value pairs.
# Example dictionary
my_dict = {'name':'John','age':30, 'city':'USA', 'gender':'Male'}

# Iterating over dictionary
for key,value in my_dict.items():
    print(f'Key:{key}, Value:{value}')

# Example 9: Merging Dictionaries
# You can merge dictionaries using the update() method or the ** operator in Python 3.9+.

# Example dictionaries
dict1 = {'name': 'John', 'age': 25}
dict2 = {'city': 'New York', 'country': 'USA'}

# Merging using update()
dict1.update(dict2)

# Printing the merged dictionary
print('Merged Dictionary :', dict1)

# Example 10: Dictionary Length
# The len() function is used to find the number of key-value pairs in a dictionary.

# Example dictionary
my_dict = {'name': 'John', 'age': 25, 'city': 'New York'}
# Getting the length of the dictionary
dict_length = len(my_dict)
print('Length of Dictionary:', dict_length)

