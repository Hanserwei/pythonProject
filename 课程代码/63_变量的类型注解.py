# 变量的类型注解
# 变量:类型
from typing import Union

# 基础数据类型注解
var1:int = 10
var2:bool = True
var3:float = 10.00
var4:str = "10"

# 类对象类型注解
class Student:
    pass
stu: Student = Student()

# 基础容器类型注解
my_list: list = [1,2,3]
my_tuple: tuple = (1,2,3)
my_set: set = {1,2,3}
my_dict: dict = {'SWJTU':211}
my_str: str = "1,2,3"

# 容器类型详细注解
my_list2: list[int] = [1,2,3]
my_tuple2: tuple[int,str,bool] = (1,"2",True)
my_set2: set[int] = {1,2,3}
my_dict2: dict[str,int] = {'SWJTU':211}

# 对于变量不用写注解,不写注解就能知道变量类型,只有当无法看出类型才添加注解

# 函数(方法)的形参的类型注解
# def 函数方法名(形参名:类型,形参名:类型,...) -> 返回值类型:
def func(data:list)-> str :
    data.append('1')
    return str(data)
func_list = []
Data = func(func_list)
print(Data)

# union类型注解
my_list3: list[Union[str,int]] = ["1",2,3]
my_dict3: dict[str,Union[str,int]] = {'SWJTU':211,'CQU':'酒吧舞'}

def func1(data:Union[str,int])-> Union[str,int] :
    print(data)
    return data

