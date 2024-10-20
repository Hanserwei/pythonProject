# python的内置方法,前面的__init__就是内置方法之一
# 魔术方法包括__init__构造方法,__str__字符串方法,__lt__小于大于符号比较,__len__小于等于,大于等于符号比较
# __eq__ ==符号比较

# 字符串方法__str__
class Student:
    def __init__(self, name,age):
        self.name = name
        self.age = age

    def __str__(self):
        return f'name:{self.name} ,age:{self.age}'

    def __lt__(self, other):
        return self.age < other.age # 只可以用于小于或者大于

    def __le__(self, other):
        return self.age <= other.age # 可以用于小于等于或者大于等于

    def __eq__(self, other):
        return self.age == other.age

stu1 = Student('周杰伦',18)
stu2 = Student('林俊杰',20)
# print(stu1)
# print(str(stu1))
#
# print(stu1<stu2)
# print(stu1>stu2)
#
# print(stu1>=stu2)
# print(stu1<=stu2)

print(stu1 == stu2)