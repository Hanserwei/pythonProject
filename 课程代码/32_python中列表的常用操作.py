# 列表常用操作包括,插入,删除,清空,追加
# 在Python中将函数定义为class的成员,那么函数就会称之为:方法
# class MyClass:
#     def add(self,x,y):
#         """
#         Purpose: 加
#         """
#         return x+y
#     # end def
# # 方法的调用
# student = MyClass()
# num = student.add(1,2)

# 列表查询方法index
# 使用方法 列表.index(元素)
# my_list = ['itcast','itheima','python']
# index = my_list.index("itheima")
# print(index)
# index2 = my_list.index("abc")
# print(index2)
# 若查询的元素不存在就会报错

# 修改特定位置(索引)的元素值
# 语法:列表[下标] = 值
# my_list = ['itcast','itheima','python']
# my_list[1] = '黑马'
# print(my_list)

# 列表中进行元素的插入
# 列表.insert(下标,元素),在指定的位置插入指定的元素
# my_list = ['itcast','itheima','python']
# my_list.insert(1,'best')
# print(my_list)
# 插入的元素的下表会变成传入的下标,列表元素后移1位

# 列表追加元素
# 列表.append(元素),将指定的元素插入到列表的尾部
# my_list = ['itcast','itheima','python']
# my_list.append('SWJTU')
# print(my_list)

# 列表追加一批元素
# 列表.extend(其他数据容器)
# my_list = ['itcast','itheima','python']
# my_list2 = [1,2,3]
# my_list.extend(my_list2)
# print(my_list)

# 列表元素的删除
# 语法1: del列表[下标]
# 语法2: 列表.pop(下标)
# my_list = ['itcast','itheima','python']
# del my_list[2]
# print(my_list)

# my_list2 = ['itcast','itheima','python']
# my_list2.pop(2)
# print(my_list2)
# 值得注意的是.pop是将对应下标的元素取出,而不是直接删除,所以可以用量取到取出的值
# my_list2 = ['itcast','itheima','python']
# word = my_list2.pop(2)
# print(my_list2)
# print(word,type(word))

# 指定列表某一个元素进行匹配删除
# 语法:列表.remove(元素)
# 传入的元素后从前到后在列表里进行搜索,删除遇到的第一个匹配元素
# my_list = [1,2,3,4,5,1,2,3]
# my_list.remove(1)
# print(my_list)

# 清空列表
# 语法: 列表.clear()
# my_list = [1,2,3,4,5,1,2,3]
# my_list.clear()
# print(my_list)

# 统计列表中的某元素含量
# 语法: 列表.count(元素)
# my_list = [1,1,1,2,3,4,1,2,3,4,5,6,'1','1']
# print(my_list.count(1))
# print(my_list.count('1'))

# 统计列表里所有元素的数量
# 使用len函数
my_list = [1,1,1,2,3,4,1,2,3,4,5,6,'1','1']
count = len(my_list)
print(count)
