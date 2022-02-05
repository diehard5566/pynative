# Exercise 7: String characters balance Test
# Write a program to check if two strings are balanced. 
# For example, strings s1 and s2 are balanced if all the characters in the s1 are present in s2. 
# The character’s position doesn’t matter.

def balance(s1, s2):
    for i in s1:
        if i in s2:
            print(True)
        else:
            print(False)        
        
    
       
    
# balance("Yn", "PYnative")
balance("Ynf", "PYnative")
# balance("at", "PYnative")
balance("atP", "PYnative")