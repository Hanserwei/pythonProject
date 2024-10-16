# 集合内部元素不重复,且无序
# 定义语法{元素,元素,...}
# 空集合:set{}

# 定义集合
my_set = {'西南交大','西安交大','北京交大'}
my_set_empty = set() 
print(my_set,type(my_set))
print(my_set_empty,type(my_set_empty))

# 集合是无序的,所有不支持下标索引访问
# 但是集合支持修改

# 添加新元素
my_set.add('重庆交大')
my_set.add('西南交大')
print(my_set)

# 移除元素
# 使用remove移除指定元素
my_set.remove('重庆交大')
print(my_set)

# 从集合取出元素
# 使用pop随机取出元素
word = my_set.pop()
print(word)
print(my_set)

# 清空集合
# 使用clear方法
my_set.clear()
print(my_set)

# 取两个集合的差集以第一个集合为基准,第二个集合比第一个集合多的元素构成一个集合
# 使用difference方法,取出
set1 = {1,2,3,4}
set2 = {1,2,3,4,5,6,7}
set3 = set1.difference(set2)
print(set1)
print(set2)
print(set3)

# 消除两个集合的差集
# 语法:集合1.difference_update(集合2)
# 对比集合1和集合2,在集合1中删除和集合2相同的元素
# 结果:集合1被修改,集合2不变

set1 = {1,2,3,4}
set2 = {1,6,7,8,9}
set1.difference_update(set2)
print(set1)
print(set2) # 集合1发生变化,集合2不变化

# 两个集合合并为一个
# 使用union方法合二为一
set1 = {1,2,3,4,5}
set2 = {1,6,7,8,9}
set3 = set1.union(set2)
print(set3)

# 统计集合的元素数量
# 使用len函数
set1 = {1,2,3,4,5,6,7,8,9,0}
print(len(set1))

# 集合的遍历
# 只可以使用while循环取遍历
set1 = {1,2,3,4,5,6,7,8,9,0}
for x in set1:
    # comment: 
    print(x)
# end for
