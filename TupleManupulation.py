# Tuple Creation

# Create a tuple named my_tuple containing at least five different elements (mix of integers, strings, and a float).
my_tuple = (10, 20, "Alice", "Bob", 45.6)

# Print the tuple.
print(my_tuple)

# Accessing Elements

# Print all elements of the tuple using unpacking.
print(*my_tuple)

# Use a loop to iterate through my_tuple and print each element.
for element in my_tuple:
    print(element)

# Print the first and last element of my_tuple using indexing.
print(my_tuple[0])
print(my_tuple[-1])

# Use negative indexing to access the second last element.
print(my_tuple[-2])

# Tuple Slicing

# Slice and print elements from index 2 to 3.
print(my_tuple[2:4])

# Slice and print the first three elements of my_tuple.
print(my_tuple[:3])

# Slice and print the last two elements in reverse order.
print(my_tuple[:-3:-1])

# Tuple Operations

# Create another tuple and perform operations.
another_tuple = (5, 15, 25, 35, 45)

# Find the length of another_tuple.
print(len(another_tuple))

# Find the maximum value in another_tuple.
print(max(another_tuple))

# Find the minimum value in another_tuple.
print(min(another_tuple))

# Find the sum of all elements in another_tuple.
print(sum(another_tuple))

# Concatenate my_tuple with another_tuple and print the result.
print(my_tuple + another_tuple)

# Repeat my_tuple twice and print the result.
print(my_tuple * 2)

# Tuple Methods

# Find the index of a specific element in my_tuple and print it.
print(my_tuple.index("Alice"))

# Count the occurrences of a specific element in my_tuple and print it.
print(my_tuple.count(20))

# Tuple Immutability

# Try changing one element in my_tuple and observe the error.
# my_tuple[2] = "Charlie"  # Uncommenting this will raise an error: TypeError: 'tuple' object does not support item assignment.

# Explain why tuples are immutable.
"""
Tuples are immutable, meaning their elements cannot be changed after creation. 
This immutability ensures that tuples are fixed in size and content, making them hashable and suitable for use as dictionary keys.
"""

# Tuple Packing and Unpacking

# Create a tuple with three elements and unpack them into individual variables.
packed_tuple = 100, 200, 300
x, y, z = packed_tuple

# Print the unpacked values.
print(x)
print(y)
print(z)

# Tuple Iteration

# Use a loop to iterate through my_tuple and print each element.
for element in my_tuple:
    print(element)

# Tuple Usage

# Write a function that returns multiple values using a tuple.
def return_tuple_elements(tup):
    first, second, third, fourth, fifth = tup
    return first, second, third, fourth, fifth

# Call the function and print the returned tuple.
print(return_tuple_elements(my_tuple))