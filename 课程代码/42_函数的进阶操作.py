# 函数的多返回值
def test_return():
    return 1,'hello',True

x,y,z = test_return() # 注意对位就行了
print(x)
print(y)
print(z)

# 函数的多种传参方式
# 位置参数,根据调用函数时的函数定义的参数位置来传递参数
def user_information(name,age,gender):
    print(f'你的名字{name}, 年龄{age}, 性别{gender}')
    return name,age,gender

user_information('Tome',20,'男')

# 关键字参数,调用函数的时候通过键=值的形式来传递参数
def user_information(name,age,gender):
    print(f'你的名字{name}, 年龄{age}, 性别{gender}')
    return name,age,gender

user_information(name='Jack',age=12,gender='男')
user_information(age=12,name='candy',gender='女')
# 可以和位置参数混用,但是位置参数必须在关键字参数的前面
user_information('小王',age=12,gender='男')

# 缺省参数,该参数叫做默认参数用于定义函数为函数提供默认值,
# 调用函数值的时候可以不传该默认值(注意:所有位置参数必须出现在默认参数的前面,包括函数的定义和调用的时候)
# 作用:当调用该函数时,没有传入参数值,就使用默认的参数值

def user_information(name,age,gender='男'):
    print(f"你的名字是{name},年龄是{age},性别是{gender}")
    return name,age,gender

user_information('Tom',20)
user_information('Rose',20,'女')

# 不定长的参数,也叫可变参数
# 位置传递的不定长
# def demo(*args):
#     print(args)
#
# demo(1)
# demo(1,2,3)
# 传递进的所有参数都会被args变量收集,它会根据传进参数的位置合并成一个元组,args是元组类型,这就是位置传递

# 关键字传递的不定长
# def demo(**kwargs):
#     print(kwargs)
#     return kwargs
#
# demo(name = 'Tom',age = 18,gender = '男')
#参数是"键=值"的情况下,所有的"键=值"都会被kwargs接受,同时根据"键=值"组成字典

def user_infor(*args):
    print(f"args的值是{args},类型是{type(args)}")

user_infor(1,2,3,'小米','男孩')

def user_infor(**kwargs):
    print(f"kwargs的值是{kwargs},类型是{type(kwargs)}")

user_infor(age=12,name='candy')

