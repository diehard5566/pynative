# Exercise 8: Find all occurrences of a substring in a given string by ignoring the case
# Write a program to find all occurrences of “USA” in a given string ignoring the case.

# Given:

str1 = "Welcome to USA. usa awesome, isn't it?"

str2 = str1.upper()
print(str2)

count = str2.count("USA")
    

print("The USA count is:", count)