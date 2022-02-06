# Exercise 18: Replace each special symbol with # in the following string
# Given:

str1 = '/*Jon is @developer & musician!!'

re = str1.replace("/","#").replace("*","#").replace("@", "#").replace("&", "#").replace("!!", "##")

print(re)