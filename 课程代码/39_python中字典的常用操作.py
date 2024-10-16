# 字典新增元素
# 语法:字典[key] = Value
my_dict = {'王力宏':99,'周杰伦':90,'林俊杰':88,'周杰伦':60}
my_dict['李宇春'] = 100
print(my_dict)

# 字典更新元素
# 语法:字典[key] = Value
my_dict['周杰伦'] = 33
print(my_dict)

# 删除元素
# 语法:字典.pop(key)
word = my_dict.pop('李宇春')
print(word)
print(my_dict)

# 清空元素
# 使用clear方法
my_dict.clear()
print(my_dict)

# 获取全部key
# 语法: 字典.keys(),结果:取得字典中的全部key
my_dict = {'王力宏':99,'周杰伦':90,'林俊杰':88,'周杰伦':60}
keys = my_dict.keys()
print(keys)

# 遍历字典
# 先用keys取得所有的key,再用key取得value
my_dict = {'王力宏':99,'周杰伦':90,'林俊杰':88,'周杰伦':60}
keys = my_dict.keys()
# 法1:使用keys遍历
for key in keys:
    # comment: 
    print(key)
    print(my_dict[key])
# end for

# 法2:直接对字典进行遍历
for key in my_dict:
    # comment: 
    print(key)
    print(my_dict[key])
# end for

# 统计字典内的元素数量
# 使用len函数
num = len(my_dict)
print(num)