
# Example 7: Tuple Comprehension (using generator expression)
# Tuples do not support comprehension like lists.
# However, you can use a generator expression to create a tuple.

# Creating a tuple of squares of numbers from 0 to 4
squared_tuple = tuple(x**2 for x in range(5))

# Printing the tuple
print('Squared Tuple:', squared_tuple)
