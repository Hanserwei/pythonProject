# python检测到错误,解释器无法继续运行了,就称为异常,俗称BUG
# 不求完美程序,但是要求在力所能及范围内保证我出现bug
# 异常捕获
# 基本语法,
# try:
#     可能发生错误的代码
# except:
#     若发生异常则执行
# 捕获异常
from tkinter.font import names

# try:
#     f = open('./测试相关文件/abcd.txt','r',encoding='utf-8')
# except:
#     print('hello world!')
# # 捕获指定类型的异常
# try:
#     print(name)
# except NameError as e:
#     print('hello world!')
#     print(e)
# # 捕获多个异常
# try:
#     print(1/0)
#     print(name)
# except (NameError, ZeroDivisionError) as e:
#     print('hello world!')
#     print(e)
# # 捕获所有的异常
# try:
#     print(1/0)
#     print(name)
#     f = open('./测试相关文件/abcd.txt', 'r', encoding='utf-8')
# except Exception as e:
#     print(e)
#     print('hello world!')
#     print(e)

try:
    print('Hello World')
except NameError as e:
    print(e) # 出现异常就会执行
else:
    print('没错') # 若没有异常就会执行
finally:
    print('结束了!') # 有无异常都会执行
# else与finally是可选元素