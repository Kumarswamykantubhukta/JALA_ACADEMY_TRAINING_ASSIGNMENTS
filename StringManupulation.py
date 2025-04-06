# Basic String Manipulation:

# Assign the string "Hello, World!" to a variable and print it.
greeting = "Hello, World!"
print(greeting)

# Create a string "Python Programming" and extract the first five characters using slicing.
language = "Python Programming"
print(language[:5])

# String Methods:

# Given a string "python is fun", convert it to uppercase.
phrase = "python is fun"
print(phrase.upper())

# Replace "fun" with "awesome" in the string "Python is fun".
updated_phrase = phrase.replace("fun", "awesome")
print(updated_phrase)

# String Formatting:

# Use f-string formatting to create a message like "My name is John, and I am 25 years old.", where the name and age are variables.
person_name = "John"
person_age = 30
print(f"My name is {person_name}, and I am {person_age} years old.")

# Given a price of 49.99, format it to display only two decimal places.
item_cost = 49.99
print("{:.2f}".format(item_cost))

# String Functions:

# Count the occurrences of the letter 'o' in "Hello, how are you?".
sentence = "Hello, how are you?"
print(sentence.count('o'))

# Find the position of "world" in "Hello, world! Python is amazing.".
text = "Hello, world! Python is amazing."
print(text.index("world"))

# Reverse and Check:

# Reverse the string "Python" using slicing.
framework = "Python"
print(framework[::-1])

# Check if "madam" is a palindrome (a word that reads the same forward and backward).
word = "madam"
if word == word[::-1]:
    print(f"{word} is a Palindrome")
else:
    print(f"{word} is not a Palindrome")