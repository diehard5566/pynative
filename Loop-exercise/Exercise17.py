# Exercise 17: Find the sum of the series upto n terms
# Write a program to calculate the sum of series up to n term. 
# For example, if n =5 the series will become 2 + 22 + 222 + 2222 + 22222 = 24690

# Given:

# # number of terms
# n = 5

num = int(input("Given number: "))

sum = 2
count = 0

for i in range(0, num):
    count += sum 
    sum = sum * 10 +2
print(count)