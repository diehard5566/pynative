# Exercise 1: Create a list by picking an odd-index items from the first list and even index items from the second
# Given two lists, l1 and l2, write a program to create a third list l3 by picking an odd-index element from the list l1 and 
# even index elements from the list l2.

# Given:

l1 = [3, 6, 9, 12, 15, 18, 21]
l2 = [4, 8, 12, 16, 20, 24, 28]

l3 = []
for odd in range(len(l1)):
    if odd % 2 != 0:
        l3.append(l1[odd])

for even in range(len(l2)):
    if even %2 == 0:
        l3.append(l2[even])

print(l3)