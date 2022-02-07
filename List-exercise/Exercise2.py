# Exercise 2: Concatenate two lists index-wise
# Write a program to add two lists index-wise. 
# Create a new list that contains the 0th index item from both the list, then the 1st index item, 
# and so on till the last element. any leftover items will get added at the end of the new list.

# Given:

list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]

new1 = []

for i in range(len(list1)):
    new = list1[i] + list2[i]
    new1.append(new)
print(new1)





