# Exercise 5: Count all letters, digits, and special symbols from a given string
# Given:

str1 = "P@#yn26at^&i5ve"

char = 0
number = 0
symbol = 0


for char1 in str1:
    if char1.isalpha():
        char = char + 1 

for num in str1:
    if num.isdigit():
        number = number + 1 

for sym in str1:
    if not sym.isalnum():
        symbol = symbol + 1
    

print("Total counts of chars, digits, and symbols ")
print("Char  = ", char)
print("Digits  = ", number)
print("Symbol  = ", symbol)