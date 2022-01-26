# Exercise 7: Return the count of a given substring from a string
# Write a program to find how many times substring “Emma” appears in the given string.

def howmany(x):
    count = 0 #因為要計算次數，所以先給一個count變數
    for i in range(len(x)): #用for迴圈 把字串列出來
        if x[i:i+4] == 'Emma':#如果在字串的->[i:i+4]裡面，有等於Emma的話
            count = count + 1 #就+1
    print('Emma appeared ' + str(count) + ' times')

sub_string = "Emma is good developer. Emma is a writer"
howmany(sub_string)#呼叫function

# str_x = "Emma is good developer. Emma is a writer"
# cnt = str_x.count("Emma")
# print('Emma appeared ' + str(cnt) + ' times')
#簡潔解法 用count方法
