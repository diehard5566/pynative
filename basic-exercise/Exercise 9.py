# Exercise 9: Check Palindrome Number
# Write a program to check if the given number is a palindrome number.

# A palindrome number is a number that is same after reverse. For example 545, is the palindrome numbers

num = input('original number ')
if num[:] == num[::-1]:#如果變數n等於反轉的n的話 [::-1]代表反轉
    print("Yes. given number is palindrome number") 
else:
    print("No. given number is not palindrome number") 




    