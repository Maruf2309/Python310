
# Example 5: Removing Elements from a Tuple
# Tuples are immutable, so elements cannot be removed directly.
# To remove elements, you need to convert the tuple to a list and back to a tuple.

# Example tuple
my_tuple = (1, 2, 3, 4)

# Converting to a list and removing an element
temp_list = list(my_tuple)
temp_list.remove(2)
my_tuple = tuple(temp_list)

# Printing the tuple after removal
print('Tuple after Removal:', my_tuple)
