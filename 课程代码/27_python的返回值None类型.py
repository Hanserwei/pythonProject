# 若函数没有return,则函数的返回值的类型是None
# def say_hi():
#     """
#     Purpose: 
#     """
    
# # end def
# r = say_hi()
# print(type(r))

# def say_hi():
#     """
#     Purpose: 
#     """
#     return None
# # end def
# r = say_hi()
# print(type(r))
# 也可以手动返回None

# None用与if判断
def check_age(age):
    """
    Purpose: 判断年龄是否满18
    """
    if (age>18):
        # comment: 
        return "success"
    else:
        # comment: 
        return None
    # end if
# end def

result = check_age(16)
if not result:
    # 进入if的值如果是None那么就代表False
    print("未成年,不能进入!")

# None可以用于声明一些没有初始内容的变量
name = None