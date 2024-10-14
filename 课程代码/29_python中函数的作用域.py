# 变量的作用域是指变量的作用范围
# 变量分为全局变量和局部变量,局部变量就只在函数体内使用
# 全局变量无法在函数体内进行修改

# 演示局部变量
# def test_a():
#     """
#     Purpose: 
#     """
#     num = 100
#     print(num)
# # end def
# test_a()
# print(num)
# 出了函数体函数就无法使用了

# 演示全局变量
# num = 100
# def test_a():
#     """
#     Purpose: 
#     """
#     print(f"test_a:{num}")
# # end def
# def test_b():
#     """
#     Purpose: 
#     """
#     print(f"test_b:{num}")
# # end def
# test_a()
# test_b()
# print(num)

# global 关键字声明变量为全局变量
num =100 
def testb():
    """
    Purpose: 
    """
    global num
    num = 200
    print(num)
# end def
testb()
print(num)