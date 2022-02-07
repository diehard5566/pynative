# Exercise 7: Checks if one set is a subset or superset of another set. If found, delete all elements from that set
# Given:

first_set = {27, 43, 34}
second_set = {34, 93, 22, 27, 43, 53, 48}

print(first_set.issubset(second_set))

print(second_set.issubset(first_set))

print(first_set.issuperset(second_set))

print(second_set.issuperset(first_set))

if first_set.issubset(second_set):
    first_set.clear()

if second_set.issubset(first_set):
    second_set.clear()

print(first_set)
print(second_set)
