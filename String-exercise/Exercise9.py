# Exercise 9: Calculate the sum and average of the digits present in a string
# Given a string s1, write a program to return the sum and average of the digits that appear in the string, 
# ignoring all other characters.

# Given:

str1 = "PYnative29@#8496"
ilst = []
count = 0

for i in str1:
    if i.isdigit():
        #print(i)
        #sum
        count += int(i)

        #make it to list to find how much is len of that number
        ilst.append(i)
        s = ''.join(ilst)
        
        avg = count / len(s)
        
print("Sum is: " + str(count) + " Average is " + str(avg))









        
