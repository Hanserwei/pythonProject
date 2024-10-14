# 函数指的是组织好的，可以重复使用的代码段。

# 统计字符串函数，不使用内置函数
str1 = "abcde"
str2 = "qwertuy"
str3 = "shdjkahskjhda"

def count_str(x):
    """
    Purpose: x
    """
    count = 0
    for i in x:
        # comment: 
        count += 1
    # end for
    print(f"字符串长度为{count}")
# end def

count_str(str1)
count_str(str2)
count_str(str3)