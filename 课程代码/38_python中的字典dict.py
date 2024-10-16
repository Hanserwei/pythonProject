# 字典包含一个key和一个value,两者一一对应
# 通过字典可以实现用key取出value的作用

# 定义字典
my_dict ={
            '王力宏':99,
            '周杰伦':90,
            '林俊杰':88
        }
# 定义空字典
dic1 = dict()
dic2 = {}
print(my_dict,type(my_dict))
print(dic1,type(dic1))
print(dic2,type(dic2))

# 字典的Key是不允许重复的
my_dict = {'王力宏':99,'周杰伦':90,'林俊杰':88,'周杰伦':60}
print(my_dict)
# 字典不允许key重复,后面的key:value会覆盖掉前面的key:value

# 从字典基于key取得value
my_dict = {'王力宏':99,'周杰伦':90,'林俊杰':88}
print(my_dict['周杰伦'])
print(my_dict['林俊杰'])

# 字典的嵌套,字典key和value可以是任何数据类型,key不能为字典
score_dict = {
    '王力宏':{'语文':77,'数学':66,'英语':33},
    '周杰伦':{'语文':88,'数学':86,'英语':55},
    '林俊杰':{'语文':99,'数学':96,'英语':66}}
print(score_dict)

# 从嵌套字典取得数据
print(f"周杰伦的语文成绩{score_dict['周杰伦']['语文']}")
print(f"林俊杰的英语成绩{score_dict['林俊杰']['英语']}")
