# 字符串定义法，单引号，双引号，三引号定义
# name = '黑马'
# name = "黑马"
# name = """黑马"""
name = '黑马程序员'
print(type(name))
name = "黑马"
print(type(name))
name = """卧室"""
print(type(name))
# 若想写的字符串包含单引号双引号自身
# 使用转移字符(\),或者单引号定义双引号，双引号定义单引号
name = '"卧室"'
print(name)
name = "'你得'"
print(name)
name = "\"黑马\""
print(name)
# 字符串拼接，通过+就可以实现拼接
# age = 11
# print("我今年"+ age)
# 注意只可以字符串进行拼接
age = 11
print("我今年"+str(age))
age = "11岁"
name = "老马"
print(age+name)
# 字符串格式化
# 占位号码，%s，可以支持字符串和数字类型的进行拼接，不用进行类型的转换
school = "SWJTU"
goal = "学电气来%s" % school
print(goal)
# 多个占位
class_num = 57
salary = 16000
print("今年毕业了%s个人,平均工资%s"% (class_num,salary))
# %s,将内容转换成字符串，放入占位位置
# %d,将内容转换成整数，放入站位位置
# %f,将内容转换成浮点型，放入占位位置
name = "博客"
setup_year = 2006
stock_price = 19.99
message2 = "%s,成立于：%d,今日的股价是%s" %(name,setup_year,stock_price)
message = "%s,成立于：%d,今日的股价是%f" %(name,setup_year,stock_price)
print(message)
print(message2)
# 若使用的是%f,那么结果的浮点数小数位数会很多位。
# 格式化中的精度控制
# 使用m.n来进行控制数据的宽度和精度，m控制宽度，很少使用，.n控制小数点的精度，要求是数字，会进行小数的四舍五入。
# 比如说%5d,表示将整数的宽度控制在五位，如数字11,输出就会变成   11,即用三个空格来补足五位。
num = 11
message = "数字是%d" % num
message2 = "数字是%5d" % num
print(message)
print(message2)
num = 11.123
message = "数字是%.1f" % num
print(message)
# .n只针对说%f占位的时候，若是%d则会转变为整数类型从而小数位数全部被舍弃
message = "数字是%5.1f" % num # 先处理小数部分，然后再处理位数部分
print(message)
# 字符串格式化的方式2
# 通过f"内容{}"
name = "张三"
age = 30
weight = 120.4567
print(f"我是{name}，今年{age}岁，体重{weight}kg")
# 不会对变量进行精度控制直接原样输出
print(f"我是{name}，今年{age}岁，体重{weight:.2f}kg")
print(f"我是{name}，今年{age}岁，体重{weight:7.2f}kg")
# 这种方式的站位，都是将变量转换为字符串再填入，不会进行精度控制，
# 若要进行精度控制需要在变量后加上(:7.2f),其中2表示的是保留小数位数，7表示的是宽度