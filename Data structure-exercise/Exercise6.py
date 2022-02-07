# Exercise 6: Find the intersection (common) of two sets and remove those elements from the first set
# See: Python Set

# Given:

first_set = {23, 42, 65, 57, 78, 83, 29}
second_set = {57, 83, 29, 67, 73, 43, 48}

new = first_set & second_set
print(new)

print(first_set - second_set)
