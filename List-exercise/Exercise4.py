# Exercise 4: Concatenate two lists in the following order
list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]

# list3 = [x + y for x in list1 for y in list2]

list3 = []

for x in list1:
    for y in list2:
        list3.append(x + y)

# n = list1[0] + list2[0]  
# n2 = list1[0] + list2[1]
# n3 = list1[1] + list2[0]
# n4 = list1[1] + list2[1]
# list3.append(n)
# list3.append(n2)
# list3.append(n3)
# list3.append(n4)

print(list3)