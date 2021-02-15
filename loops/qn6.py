#  Write a Python program to count the number of even
#  and odd numbers from a series of numbers.
# Sample numbers : numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
# Expected Output :
# Number of even numbers : 5
# Number of odd numbers : 4

even_count = 0
odd_count = 0
numbers = list(range(1, 10))
for i in numbers:
    if i % 2 == 0:
        even_count += 1
    if i % 2 != 0:
        odd_count += 1
print(f"Number of odd numbers: {odd_count}")
print(f"Number of even numbers: {even_count}")
