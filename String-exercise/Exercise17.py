# Exercise 17: Find words with both alphabets and numbers
# Write a program to find words with both alphabets and numbers from an input string.

# Given:

str1 = "Emma25 is Data scientist50 and AI Expert"

sp = str1.split()

for i in sp:
    if not i.isalpha():
        print(i)
        