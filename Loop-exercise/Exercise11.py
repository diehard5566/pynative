# Exercise 11: Write a program to display all prime numbers within a range
# Note: A Prime Number is a number that cannot be made by multiplying other whole numbers. 
# A prime number is a natural number greater than 1 that is not a product of two smaller natural numbers

# Examples:

# 6 is not a prime mumber because it can be made by 2×3 = 6
# 37 is a prime number because no other whole numbers multiply together to make it.
# Given:

# range
start = 25
end = 50

for i in range(25, 51):
    if i % 2 ==0:
        pass
    else:
        print(i)
