# Exercise 2: Print the sum of the current number and the previous number
# Write a program to iterate the first 10 numbers and in each iteration, print the sum of the current and previous number.

sum = 0
for i in range(0, 9):
    if i == 0:
        print(0)
    sum = i + (i+1)
    print(sum)