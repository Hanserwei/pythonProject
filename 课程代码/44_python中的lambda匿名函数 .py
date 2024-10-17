# def 定义的函数是带有名字的函数,可以反复调用
# lambda 定义的函数是匿名函数(没有名字),只可以临时使用一次
# 语法 lambda 形参1,形参2,...: x ,y ,...

def test_function(compute):
    result = compute(1,2)
    print(result)

test_function(lambda x,y:x+y)
# 其实就是lambda作为一个逻辑函数传入