# Exercise 16: Removal all characters from a string except integers
# Given:

str1 = 'I am 25 years and 10 months old'

ls = []
for i in str1:
    if i.isdigit():
        ls.append(i)

str2 = "".join(ls)

print(str2)