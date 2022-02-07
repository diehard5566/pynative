# Exercise 9: Get all values from the dictionary and add them to a list but don’t add duplicates
# Given:


speed = {'jan': 47, 'feb': 52, 'march': 47, 'April': 44, 'May': 52, 'June': 53, 'july': 54, 'Aug': 44, 'Sept': 54}

new_list = []

#用.values方法 配合 for loop把dict裡的value拿出來
for value in speed.values():
    #再append進新的list
    new_list.append(value)
    #用set()來拿掉重複的元素
    new = list(set(new_list))       
print(new)