# Exercise 2: Remove and add item in a list
# Write a program to remove the item present at index 4 and add it to the 2nd position and at the end of the list.

# Given:

list1 = [54, 44, 27, 79, 91, 41]

list2 = list1[0:4] + list1[5:]
print(list2)

list2.insert(2, 11)

print(list2)

list2.append(11)

print(list2)
