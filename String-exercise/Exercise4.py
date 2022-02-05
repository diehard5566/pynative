# Exercise 4: Arrange string characters such that lowercase letters should come first
# Given string contains a combination of the lower and upper case letters. 
# Write a program to arrange the characters of a string so that all lowercase letters should come first.

# Given:

# str1 = PyNaTive

def lowfirst(str1):
    #find lower case in string
    newstr = []
    for i in str1:
        if i.islower():
            newstr.append(i)
   
    #.join() combine string
    low = ''.join(newstr)

    newstr2 = []
    for j in str1:
        if j.isupper():
            newstr2.append(j)

    up = ''.join(newstr2)

    lowfirst1 = low + up
    print(lowfirst1)

lowfirst("PyNaTive")