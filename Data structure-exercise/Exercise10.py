# Exercise 10: Remove duplicates from a list and create a tuple and find the minimum and maximum number
# Given:

sample_list = [87, 45, 41, 65, 94, 41, 99, 94]

re = list(set(sample_list))
print(re)

tu = tuple(re)
print(tu)

print(min(tu))
print(max(tu))