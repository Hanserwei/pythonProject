# 数据容器的类型转换
my_list = [1,2,3]
my_tuple = (1,2,3,4,5)
my_str = 'atheism'
my_set = {1,2,3,4,5}
my_dict = {'key1':1,'key2':2,'key3':3,'key4':4,'key5':5}
# 类型转换:容器转列表
print(f"列表转列表的结果是{list(my_list)}")
print(f"元组转列表的结果是{list(my_tuple)}")
print(f"字符串转列表的结果是{list(my_str)}")
print(f"集合转列表的结果是{list(my_set)}")
print(f"字典转列表的结果是{list(my_dict)}")
# 字符串转列表,将每个字符转换成list的元素,字典转list则value会被抛弃
# 类型转换:容器转元组
print(f"列表转元组的结果是{tuple(my_list)}")
print(f"元组转元组的结果是{tuple(my_tuple)}")
print(f"字符串转元组的结果是{tuple(my_str)}")
print(f"集合转元组的结果是{tuple(my_set)}")
print(f"字典转元组的结果是{tuple(my_dict)}")
# 字符串转元组将字符串的每个字符都取出作为元素,字典的Value也会被抛弃
# 类型转换:容器转字符串
print(f"列表转字符串的结果是{str(my_list)}")
print(f"元组转字符串的结果是{str(my_tuple)}")
print(f"字符串转字符串的结果是{str(my_str)}")
print(f"集合转字符串的结果是{str(my_set)}")
print(f"字典转字符串的结果是{str(my_dict)}")
# 类型转换:容器转集合
print(f"列表转集合的结果是{set(my_list)}")
print(f"元组转集合的结果是{set(my_tuple)}")
print(f"字符串转集合的结果是{set(my_str)}")
print(f"集合转集合的结果是{set(my_set)}")
print(f"字典转集合的结果是{set(my_dict)}")

# 容器的通用排序功能
# sorted(容器,[reverse = True])
my_list = [3,4,1,6,8,0]
my_tuple = (0,6,3,8,9)
my_str = 'atheism'
my_set = {5,7,2,1,4,6}
my_dict = {'key1':6,'key2':4,'key3':2,'key4':1,'key5':0}
print(f"列表对象排序的结果是{sorted(my_list)}")
print(f"元组对象排序的结果是{sorted(my_tuple)}")
print(f"字符串对象排序的结果是{sorted(my_str)}")
print(f"集合对象排序的结果是{sorted(my_set)}")
print(f"字典对象排序的结果是{sorted(my_dict)}")
# 排序的结果都会变成列表对象,即对容器进行排序并存入一个列表,字典排序也同样会丢失Value
print(f"列表对象排序的结果是{sorted(my_list,reverse=True)}")
print(f"元组对象排序的结果是{sorted(my_tuple,reverse=True)}")
print(f"字符串对象排序的结果是{sorted(my_str,reverse=True)}")
print(f"集合对象排序的结果是{sorted(my_set,reverse=True)}")
print(f"字典对象排序的结果是{sorted(my_dict,reverse=True)}")
