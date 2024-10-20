# 一行代码完成对类对象的属性进行赋值

# 使用构造方法__init__方法使用
# 可以实现:
# 在创建类对象的时候,会自动执行
# 在创建类对象的适合,将传入的参数自动传递给__init__方法使用

class Student:
    name = None # 可以省略
    age = None # 可以省略
    tel = None # 可以省略

    def __init__(self, name, age, tel):
        self.name = name
        self.age = age
        self.tel = tel
        print('Student object created!')

stu = Student('周杰伦',18,114514)
print(stu.name)
print(stu.age)
print(stu.tel)