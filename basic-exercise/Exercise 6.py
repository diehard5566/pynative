# Exercise 6: Display numbers divisible by 5 from a list
# Iterate the given list of numbers and print only those numbers which are divisible by 5

def div5(lst):
    print('Given list is ', lst) #在第一行印出string and list
    print('Divisable by 5')

    for i in lst:
        if i % 5 == 0:
            print([i])
            
lst1 = [10, 20, 33, 46, 55]

div5(lst1)


