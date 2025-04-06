# Even or Odd Checker:
# Write a Python program that takes an integer input from the user and determines whether the number is even or odd using an if-else statement.
number = int(input("Enter a number to check if it's even or odd: "))
if number % 2 == 0:
    print("The number is Even.")
else:
    print("The number is Odd.")

# Find the Largest Number:
# Create a Python program that takes three numbers as input and uses if-else conditions to find and display the largest number.
x, y, z = map(int, input("Enter three numbers separated by spaces: ").split())
if x > y and x > z:
    print("The largest number is:", x)
elif y > z:
    print("The largest number is:", y)
else:
    print("The largest number is:", z)

# Number Classification:
# Write a program that takes a number input and checks if the number is positive, negative, or zero using if-elif-else conditions.
num = int(input("Enter a number to classify: "))
if num > 0:
    print("The number is Positive.")
elif num < 0:
    print("The number is Negative.")
else:
    print("The number is Zero.")

# Sum of Numbers in a Range:
# Write a Python program that takes two numbers (start and end) as input and uses a for loop to compute and display the sum of all numbers in that range.
total = 0
start_range = int(input("Enter the start of the range: "))
end_range = int(input("Enter the end of the range: "))
for i in range(start_range, end_range + 1):
    total += i
print("The sum of numbers in the range is:", total)

# Printing a Multiplication Table:
# Develop a Python program that takes an integer as input and prints its multiplication table from 1 to 10 using a for loop.
table_number = int(input("Enter a number to print its multiplication table: "))
for i in range(1, 11):
    print(f"{table_number} x {i} = {table_number * i}")

# Counting Vowels in a String:
# Write a Python script that takes a string input from the user and uses a for loop to count the number of vowels (a, e, i, o, u) present in the string.
vowel_count = 0
vowel_list = "aeiou"
user_string = input("Enter a string to count the vowels: ")
for char in user_string:
    if char in vowel_list:
        vowel_count += 1
print("The number of vowels in the string is:", vowel_count)

# Factorial of a Number:
# Write a Python program to calculate the factorial of a number using a for loop.
factorial_number = int(input("Enter a number to calculate its factorial: "))
factorial_result = 1
for i in range(1, factorial_number + 1):
    factorial_result *= i
print("The factorial of the number is:", factorial_result)

# FizzBuzz Game:
# Write a Python program that prints numbers from 1 to 50. However:
# For multiples of 3, print "Fizz" instead of the number.
# For multiples of 5, print "Buzz".
# For numbers that are multiples of both 3 and 5, print "FizzBuzz".
for num in range(1, 51):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)

# Printing a Pattern:
# Write a Python program to print the following pattern using nested loops:
# *
# * *
# * * *
# * * * *
# * * * * *
for row in range(1, 6):
    for col in range(row):
        print("*", end=' ')
    print()