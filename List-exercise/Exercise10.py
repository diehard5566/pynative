# Exercise 10: Remove all occurrences of a specific item from a list.
# Given a Python list, write a program to remove all occurrences of item 20.

# Given:

list1 = [5, 20, 15, 20, 25, 50, 20]

for i in list1:
    if i == 20:
        list1.remove(20)
print(list1)


