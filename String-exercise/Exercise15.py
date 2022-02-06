# Exercise 15: Remove special symbols / punctuation from a string
# Given:

str1 = "/*Jon is @developer & musician"

# ls = []
# for i in str1:
#     if i.isalnum():
#         ls.append(i)

# str2 = "".join(ls)

# print(str2)

sp = str1.split()

p = sp.pop(0)

p1 = sp.pop(0)

p2 = sp.pop(0)

p3 = sp.pop(1)

pj = p[2:]
pd = p2[1:]
print(pj, p1, pd, p3)




