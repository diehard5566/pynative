# Exercise 5: Create a Python set such that it shows the element from both lists in a pair
# Given:

first_list = [2, 3, 4, 5, 6, 7, 8]
second_list = [4, 9, 16, 25, 36, 49, 64]

# res = []

# for i in first_list:
#     for j in second_list:
#         if j == i*i:
#             res.append((i,j))
#             set_res = set(res)

# print(set_res)

res = zip(first_list, second_list)
ress = set(res)
print(ress)

