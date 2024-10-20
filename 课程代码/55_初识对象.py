# 数据的组织

# 设计类
class student:
    name = None
    gender = None
    nationality = None
    native_place = None
    age = None

# 基于类创建对象
stu_1=student()
stu_2=student()

# 为对象属性赋值
stu_1.name = '林俊杰'
stu_1.gender = '男'
stu_1.nationality = '中国'
stu_1.native_place = '山东省'
stu_1.age = 18

# 输出对象记录的信息
print(stu_1.name)
print(stu_1.gender)
print(stu_1.nationality)
print(stu_1.native_place)
print(stu_1.age)
