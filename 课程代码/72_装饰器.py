# 装饰器也是一种闭包，其功能就是在不破坏目标函数原有的代码和功能的前提下，为目标函数增加新功能。
import random
import time

# import time
# def sleep():
#     print("睡眠中。。。。")
#     time.sleep(random.randint(1, 5))
# 希望给sleep函数，增加一个功能：
# 在调用sleep前输出:我要睡觉了
# 在调用sleep后输出:我起床了

# 装饰器一般写法（闭包写法）

# def outer(func):
#     def inner():
#         print('我要睡觉了！')
#         func()
#         print('我起床了！')
#     return inner

# def sleep():
#     print("睡眠中。。。。")
#     time.sleep(random.randint(1, 5))
#
# fn = outer(sleep) # 调用的是outer使用里面的inner函数，inner函数目前是sleep函数
# fn()

# 装饰器语法糖
def outer(func):
    def inner():
        print('我要睡觉了！')
        func()
        print('我起床了！')
    return inner

@outer
def sleep():
    print("睡眠中。。。")
    time.sleep(random.randint(1,5))


sleep()