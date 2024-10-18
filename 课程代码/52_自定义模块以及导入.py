# from my_module import test
# test(1,2)

# 导入不同模块的同名功能
# from my_module2 import test
# from my_module import test
# test(1,2)

# __main__变量
# 使用这个变量可以保证模块代码内的测试语句不会在被引用的时候运行
from my_module import test

# __all__变量
from my_module2 import *
# 使用__all__变量可以在使用*导入的时候,选择部分功能被导入
test(1,2)