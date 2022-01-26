# Exercise 1: Calculate the multiplication and sum of two numbers
#  Given two integer numbers return their product only if the product is greater than 1000, else return their sum.

num1 = int(input("type nums1 here:"))
num2 = int(input("type nums2 here:"))

product = num1 * num2
sum = num1 + num2 

if product <= 1000:
    print(product) 
else:
    print(sum)

