# Exercise 6: Count the total number of digits in a number
# Write a program to count the total number of digits in a number using a while loop.

# For example, the number is 75869, so the output should be 5.

number = str(input("Type here: "))

count = 0
digit = len(number)-1

while count <= digit:
    count = count + 1
print(count)
