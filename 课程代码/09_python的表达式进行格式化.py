# 表达式表示有明确执行结果的代码语句
print("1*1的结果是%d , 10*3的结果是%d" % (1*1, 10*3))
print(f"3+5的结果是{3+5}")
print("字符串在python中的类型是%s" % (type("object"))) # type()操作之后，结果已经是type类型了所有只可以用%s
# print(type(type("object")))