# 数据类型在特定的场景之下，数据类型是可以相互转换的，比如数字转字符串，字符串转数字
# int(x)把x转换成一个整数
# float(x)把x转换成一个浮点数
# str(x)把x转换成字符串
# 这三个和type()一样是带有结果的，可以被print输出

# 数字类型转换成字符串
num_str = str(11)
print(type(num_str))
print(num_str)
# 浮点数转字符串
float_num = str(13.14)
print(type(float_num))
print(float_num)
# 字符串转换成数字
num = int("11")
print(type(num),num)

num2 = float("11.11")
print(type(num2),num2)
# 字符串转数字要保证字符串的内容全部是数字才可以

# 整数转浮点数
float_num2 = float(11)
print(type(float_num),float_num2)
# 浮点数转整数类型
int_num2 = int(13.13)
print(type(int_num2),int_num2)