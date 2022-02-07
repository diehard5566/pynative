# Exercise 8: Generate a Python list of all the even numbers between 4 to 30

def gen(num1,num2):
    lst = []
    for i in range(num1, num2):
        if i % 2 == 0:
            lst.append(i)
    print(lst)

gen(4,30)
