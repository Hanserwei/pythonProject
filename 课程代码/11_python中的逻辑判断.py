# 布尔类型的字面量：True和False
# 通过比较运算也可以得到布尔类型的结果
# result = 10>5
# print(result)
# result = "abcd" == "abcde"
# print(result)
# 在python里逻辑运算符有==，！=，>,<,>=,<=这六个运算符
bool_1 = True
bool_2 = False
print(f"bool_1的变量内容是{bool_1},类型是{type(bool_1)}")
print(f"bool_1的变量内容是{bool_2},类型是{type(bool_2)}")
# 比较运算符的使用
num1 = 10
num2 = 10
num3 = 15
num4 = 8
print(f"10==10的运算结果是{num1==10}")
print(f"10!=15的运算结果是{num1!=num3}")
name1 = "itcast"
name2 = "itheima"
print(f"namme1==name2的结果是{name1==name2}")
print(f"10>=10的结果是{num1>=num2}")
print(f"10>=15的结果是{num1>=num3}")