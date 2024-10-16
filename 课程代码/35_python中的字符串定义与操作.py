# 字符串是字符的数据容器,每个字符就是元素
# 字符串无法修改指定下标的元素,也不能移除指定下标的元素,也不能追加字符

# 通过下标索引
name = 'hanserwei'
print(name[0])
print(name[1])
print(name[-1])

# index方法
value = name.index("s")
print(f"{value}")

# replace方法
# 将字符串内的元素1替换成元素2,得到一个新字符串
new_name = name.replace("h","H")
print(new_name)

# split方法
# 按照指定的分隔字符串,将字符串分割为多个字符串,并存入列表对象中
# 注意:字符串本身不变只是得到一个新的列表

my_str = "hello my school"
my_str_list = my_str.split(' ')
print(my_str_list)

# strip方法
# 去除字符串前后空格()使用.strip()
# 去除指定的元素
# 对于第二个情况,会去除每个元素比如.strip('123'),那么1 2 3都会去除
my_str = "   hello world   "
new_my_str = my_str.strip()
print(new_my_str)
my_str = "123hello world321"
new_my_str_2 = my_str.strip('123')
print(new_my_str_2)

# 统计某个字符的出现次数,使用count方法
num = my_str.count('o')
print(num)

# 统计字符串的长度使用len函数
print(len(my_str))

# 字符串的遍历同样是用while循环或者for循环实现
# 详情见练习19