# Exercise 4: Initialize dictionary with default values
# In Python, we can initialize the keys with the same values.

# Given:

employees = ['Kelly', 'Emma']
defaults = {"designation": 'Developer', "salary": 8000}

di_em = dict(zip(employees, defaults))

di_em['Kelly'] = defaults
di_em['Emma'] = defaults

print(di_em)