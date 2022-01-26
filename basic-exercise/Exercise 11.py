# Exercise 11: Write a Program to extract each digit from an integer in the reverse order.
# For example, If the given int is 7536, the output shall be “6 3 5 7“, with a space separating the digits.

def ex11(num):
    num2 = str(num)
    print(num2[3] + ' ' + num2[2] + ' ' + num2[1] + ' ' + num2[0] )
       

ex11(7536)