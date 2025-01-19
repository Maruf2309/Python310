# Example 5: Removing Elements from a List
# You can remove elements from a list using remove() and pop().
# remove() deletes the first occurrence of a value, while pop() removes an element by index.

# Example list
my_list = ['a', 'b', 'c', 'd']

# Removing elements
my_list.remove('b')
popped_item = my_list.pop(2)

# Printing the list after removal
print('List after Removal:', my_list)
print('Popped Item:', popped_item)