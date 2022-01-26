# Exercise 3: Print characters from a string that are present at an even index number
# Write a program to accept a string from the user and display characters that are present at an even index number.

# For example, str = "pynative" so you should display ‘p’, ‘n’, ‘t’, ‘v’.

even_ind = str(input('Orginal String is  '))

print('Printing only even index chars')

even = even_ind[::2]

for i in even:
    print(i)


