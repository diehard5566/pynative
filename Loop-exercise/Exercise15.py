# Exercise 15: Use a loop to display elements from a given list present at odd index positions
# Given:

my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

for i in range(len(my_list)):
    odd_num = my_list[1:i+1:2]

for j in odd_num:
    print(j, end=" " )