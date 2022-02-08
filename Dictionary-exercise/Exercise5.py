# Exercise 5: Create a dictionary by extracting the keys from a given dictionary
# Write a Python program to create a new dictionary by extracting the mentioned keys from the below dictionary.

# Given dictionary:

sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"}

# Keys to extract
keys = ["name", "salary"]

# sample_dict.pop("age")
# sample_dict.pop("city")

# print(sample_dict)

new = {}

for i in sample_dict:
    if i == "name" or i == "salary":
        new[i] = sample_dict[i]
print(new)

# i = "name" 
# if i in sample_dict.keys():
#     new[i]= sample_dict[i]
# j = "salary"
# if j in sample_dict.keys():
#     new[j] = sample_dict[j]
#     print(new)

#----------------------------------------

# newDict = {k: sampleDict[k] for k in keys}
# print(newDict)

#----------------------------------------

# res = dict()

# for k in keys:
#     # add current key with its value from sample_dict
#     res.update({k: sample_dict[k]})
# print(res)
        
    




