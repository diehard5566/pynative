# Exercise 10: Write a program to count occurrences of all characters within a string
# Given:

str1 = "apple"

# create a result dictionary
char_dict = dict()

for char in str1:
    count = str1.count(char)
    # add / update the count of a character
    char_dict[char] = count # char = key , count = value 
    print('Result:', char_dict)