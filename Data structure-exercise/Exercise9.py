# Exercise 9: Get all values from the dictionary and add them to a list but don’t add duplicates
# Given:


speed = {'jan': 47, 'feb': 52, 'march': 47, 'April': 44, 'May': 52, 'June': 53, 'july': 54, 'Aug': 44, 'Sept': 54}

new_list = []

for value in speed.values():

    new_list.append(value)
    new = list(set(new_list))       
print(new)