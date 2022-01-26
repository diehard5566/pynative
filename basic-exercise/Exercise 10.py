#  Exercise 10: Create a new list from a two list using the following condition

# Given a two list of numbers, write a program to create a new list such that the new list 
# should contain odd numbers from the first list and even numbers from the second list.

def two_list(a, b):
    new_lst = []
    for i in a:
        if i % 2 != 0:
            new_lst.append(i)

    for j in b:
        if j % 2 == 0:
            new_lst.append(j)

    print('result list: ', new_lst)
              

list1 = [10, 20, 25, 30, 35]
list2 = [40, 45, 60, 75, 90]

two_list(list1, list2)