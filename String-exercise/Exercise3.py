# Exercise 3: Create a new string made of the first, middle, and last characters of each input string
# Given two strings, s1 and s2, write a program to return a new string made of s1 and s2’s first, 
# middle, and last characters.

# Given:

# s1 = "America"
# s2 = "Japan"

def newstr(s1, s2):
    head = s1[0] + s2[0]

    mi = int(len(s1)/2)
    mi2 = int(len(s2)/2)

    mid = s1[mi] + s2[mi2] 

    last = s1[-1] + s2[-1]
    
    s3 = head + mid + last
    print(s3)

newstr("America", "Japan")
