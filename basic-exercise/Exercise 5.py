# Exercise 5: Check if the first and last number of a list is the same
# Write a function to return True if the first and last number of a given list is same. 
# If numbers are different then return False.

def nums(lst):
    print("Given list:", lst)
    return lst[0] == lst[-1]


numbers_x = [10, 20, 30, 40, 10]
print('result is ', nums(numbers_x))

numbers_y = [75, 65, 35, 75, 30]
print('result is ' , nums(numbers_y))