# Exercise 3: Return multiple values from a function
# Write a program to create function calculation() such that it can accept two variables 
# and calculate addition and subtraction. Also, it must return both addition and subtraction in a single return call.

# Given:

def calculation(a, b):
    # Your Code
    sum =a + b
    minus = a - b
    return sum, int(minus)
    
    
res = calculation(40, 10)
print(res)

