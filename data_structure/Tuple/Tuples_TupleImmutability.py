
# Example 3: Tuple Immutability
# Tuples are immutable, meaning their values cannot be changed once created.
# Trying to modify an element of a tuple will result in an error.

# Example tuple
my_tuple = (1, 2, 3)

# Trying to modify an element (this will raise an error)
try:
    my_tuple[0] = 10
except TypeError as e:
    print('Error:', e)
