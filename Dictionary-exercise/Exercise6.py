# Exercise 6: Delete a list of keys from a dictionary
# Given:

sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"
}

# Keys to remove
keys = ["name", "salary"]

for i in keys:
    #del sample_dict[i] 也可以這樣用
    sample_dict.pop(i)

print(sample_dict)
