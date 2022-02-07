# Exercise 8: Iterate a given list and check if a given element exists as a key’s value in a dictionary. 
# If not, delete it from the list
# Given:


roll_number = [47, 64, 69, 37, 76, 83, 95, 97]
sample_dict = {'Jhon':47, 'Emma':69, 'Kelly':76, 'Jason':97}

new = []
#先把dict iterate
for j in sample_dict.items():
    #再把list iterate
    for i in roll_number:
        if i in j:
            new.append(i)
print(new)

