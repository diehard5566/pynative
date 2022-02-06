# Exercise 14: Remove empty strings from a list of strings
# Given:

str_list = ["Emma", "Jon", "", "Kelly", None, "Eric", ""]


# str_list.remove("")
# str_list.remove("")
# str_list.remove(None)

# print(str_list)

for i in str_list:
    if i == "":
        str_list.remove(i)
    elif i == None:
        str_list.remove(i)
        
print(str_list)