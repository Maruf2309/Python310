
# Example 3: Removing Elements from a Set
# You can remove elements using the remove() or discard() methods.
# The remove() method raises an error if the element is not found, while discard() does not.

# Example set
my_set = {1, 2, 3, 4}

# Removing an element
my_set.remove(2)

# Discarding an element (no error if element not found)
my_set.discard(5)

# Printing the set after removal
print('Set after Removal:', my_set)
