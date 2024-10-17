def test_function(compute):
    result = compute(1,2)
    print(type(compute))
    print(result)

def compute(x,y):
    return x+y

test_function(compute)

# 实际上是计算逻辑的传递,而非数据的传递.
# 函数作为参数传入是传入代码的执行逻辑
# 本例子中,计算逻辑由compute决定,传入的数据由test_function决定

