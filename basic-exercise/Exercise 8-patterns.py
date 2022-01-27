# Exercise 8: Print the following pattern

# print("""
# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5 
# """)
#-------------------------------------------------------
# rows = 5 #預設要幾行

# for i in range(1,rows + 1):#最外層的行就是預設的range + 1
#     for j in range(i):#列
#         print(i , end=' ')
#     print() #用來換行
#-------------------------------------------------------
#如果是要反轉的話可以用下面的程式
#-------------------------------------------------------
# rows = 5
# b = 0 #用來反轉for loop從5->0

# for i in range(rows , 0, -1): #從最後面loop回來到0
#     b += 1 
#     for j in range(1, i + 1):
#         print(b, end = " ")
#     print("")
#-------------------------------------------------------
# 同樣數字反轉圖形
# rows = 5
# num = rows

# for i in range(rows, 0, -1):
#     for j in range(0, i):
#         print(num, end=" ")#num=rows的話就會印出全部同樣數字
#     print("\r")
#-------------------------------------------------------
# 第一行從0開始
# rows = 5
 
# for i in range(rows , 0, -1): #從最後面loop回來到0 
#     for j in range(0, i + 1):
#         print(j, end = " ")
#     print(" ")
#-------------------------------------------------------
# 用while loop來印出patterns 13579
# rows = 5
# i = 1
# while i <= rows:
#     j = 1
#     while j <= i:
#         print((i * 2 - 1), end=" ")
#         j = j + 1
#     i = i + 1
#     print(' ')
#-------------------------------------------------------
# 用for loop來印出遞減數字的倒金字塔
# rows = 5

# for i in range(rows, 0, -1):
#     num = i 
#     for j in range(0, i):
#         print(num, end=" ")
#     print("\r")
#-------------------------------------------------------
# 用for loop來印出遞減數字的金字塔 12345 1234 123 12 1
# rows = 6
# for i in range(1, rows):
#     for j in range(i, 0, -1):
#         print(j, end=' ')
#     print("")
#-------------------------------------------------------
# 用for loop來印出遞減數字的倒金字塔 54321 4321 321 21 1
rows = 5
for i in range(0, rows + 1):
    for j in range(rows - i, 0, -1):
        print(j, end=' ')
    print()

