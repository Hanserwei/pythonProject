# 列表通过[]进行表示,在[]内部进行元素存储,用,隔开。
# 空列表=[]或者list()
# name_list = ['abc','222','444']
# print(name_list)
# print(type(name_list))

# my_list = ['你好!',333,True]
# print(my_list)
# print(type(my_list))

# my_list2 = [[1,1,1],[2,2,2,2],'name']
# print(my_list2)

# 注意列表内的元素无类型要求,列表内也可以是列表。称之为列表嵌套。

# 通过下标索引来取出对应位置的数据
# 下标索引不能超出索引范围
# 下标索引,列表从左往右开始,下标从0开始向右加1
# name_list = ['abc','222','444']
# print(name_list[0])
# print(name_list[1])
# print(name_list[2])
# 同样列表也可以从右向左进行索引,从右向左依次是-1,-2,-3,...
# print(name_list[-1])
# print(name_list[-2])
# print(name_list[-3])
# 对于嵌套的列表,也可以索引,下标索引相同
my_list2 = [[1,2,3],[4,5,6]]
print(my_list2[0][0])
print(my_list2[0][1])
print(my_list2[0][2])
print(my_list2[1][0])
print(my_list2[1][1])
print(my_list2[1][2])