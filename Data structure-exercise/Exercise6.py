# Exercise 6: Find the intersection (common) of two sets and remove those elements from the first set
# See: Python Set

# Given:

first_set = {23, 42, 65, 57, 78, 83, 29}
second_set = {57, 83, 29, 67, 73, 43, 48}

#用Intersection方法 找出兩個set有交集的地方
new = first_set & second_set
print(new)
#用difference方法 A-B可以得出AB相同地方以外的數值
print(first_set - second_set)
