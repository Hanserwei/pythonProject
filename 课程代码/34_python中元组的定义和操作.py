# 元组通俗认为就是一个只读的list
# 元组的定义语法是(元素,元素,元素,元素,...)
# 空元组定义()或者tuple()

# 定义元组
t1 = (1,'hello',True)
t2 = ()
t3 = tuple()
print(f"t1的类型是{type(t1)},内容是{t1}")
print(f"t2的类型是{type(t2)},内容是{t2}")
print(f"t3的类型是{type(t3)},内容是{t3}")

# 定义单个元素元组
t4 = ("hello", ) # 单个元素的元组必须后面加一个,和空格
print(f"t4的类型是{type(t4)},内容是{t4}")

# 元组的嵌套
t5 = ((1,2,3),(4,5,6))
print(f"t5的类型是{type(t5)},内容是{t5}")

# 下标索引去取出内容
num = t5[1][2]
print(num)

# 元组的操作,index,count,len
t6 = (1,1,2,3,4,4,5,6,7,7,7,8,9,10)
index = t6.index(1) # 只会找到最开始的一个符合条件的元素的下标
print(f"在元组中查找到1的下标为{index}")

count = t6.count(7)
print(f"一共有{count}个7")

length = len(t6)
print(f"{t6}元组有{length}个")

# 元组的遍历:while
t7 = (1,1,2,3,4,4,5,6,7,7,7,8,9,10)
i = 0
while i < len(t7):
    # comment: 
    print(f"元素{t7[i]}")
    i += 1
# end while

# 元组遍历:for
for x in range(0,len(t7)):
    # comment: 
    print(f"元素为{t7[x]}")
# end for

# 元组不能内的元素不能修改,但如果存的元素是list,那么list的内容可以修改
t8 = (1,[1,3])
print(t8)
t8[1][0] = 2
print(t8)