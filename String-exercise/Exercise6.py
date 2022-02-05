# Exercise 6: Create a mixed String using the following rules
# Given two strings, s1 and s2. Write a program to create a new string s3 made of the first char of s1, 
# then the last char of s2, Next, the second char of s1 and second last char of s2, and so on. 
# Any leftover chars go at the end of the result.

# Given:

# s1 = "Abc"
# s2 = "Xyz"

def mixed(s1, s2):
    mix1 = s1[0] + s2[-1]
    mix2 = s1[1] + s2[-2]
    mix3 = s1[2] + s2[-3]
    mix = mix1 + mix2 + mix3
    print(mix)

mixed("Abc", "Xyz")