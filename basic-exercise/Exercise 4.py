# Exercise 4: Remove first n characters from a string
# Write a program to remove characters from a string starting from zero up to n and return a new string.

def ex_4(str, n):
    new_str = str[n:]
    return new_str

print(ex_4("pynative", 4))
print(ex_4("pynative", 2))