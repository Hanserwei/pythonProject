# 类的定义和使用方法

# class 类的名称:
#     类的属性 # 类中的变量(成员变量)
#
#     类的行为 # 类中的函数(成员方法)

# 创建类对象的语法
# 对象 = 类名称()

# class student:
#     name = None # 学生姓名
#     age = None # 学生年龄
#     def say_hello(self):
#         print(f'大家好,我是{self.name}')

# 写在类内部的函数叫做方法
# 成员方法的定义语法

# def 方法名(self,形参1,形参2,...)
# 成员方法使用类内的成员需要使用self参数,self参数必须存在,但是调用的时候不一定需要

class Student:
    name = None
    def say_hello(self):
        print(f"大家好我是{self.name}")
        return

    def say_hello2(self,msg):
        print(f'大家好我是{self.name},{msg}')

student1 = Student()
student1.name = '周杰伦'
student1.say_hello()
student2 = Student()
student2.name = '林俊杰'
student2.say_hello()
student1.say_hello2('我是你爹!')
student2.say_hello2('我不是你爹!')
