# python中一个模块就是一个python代码的py文件,模块能定义函数类变量
# 模块就是一个工具包,可以调用出来用
# [from 模块名] import [模块|类|变量|函数|*] [as 别名]
import time #导入python的内置time模块
# time.sleep(10)
print('时间到')
# 使用from导入time的sleep功能(函数)
from time import sleep
sleep(1)
print('时间到')
# 使用*导入time模块中的全部功能
from time import *
sleep(1)
# 使用as给特定功能加上别名
import time as t
t.sleep(1)
from time import sleep as sl
sl(1)