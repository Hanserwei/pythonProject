# 本质上python包就是一个文件夹,文件夹里面有个__init__.py的文件

# 导入自定义包内的模块
import 课程代码.my_package.my_module1
# import 课程代码.my_package.my_module2
# from 课程代码 import my_package
#
# my_package.my_module1.info_print1()
# my_package.my_module2.info_print2()
#
#
# from 课程代码.my_package.my_module1 import info_print1
# from 课程代码.my_package.my_module2 import info_print2
#
# info_print1()
# info_print2()

# 通过__all__变量,控制import * 能导入的内容
from 课程代码.my_package import *
my_module1.info_print1()