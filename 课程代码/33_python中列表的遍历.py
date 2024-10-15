# 使用while循环进行遍历列表
list_1 = [1,2,3,4,5,6,7,8,9,10,11]
def list_while(list_1):
    """
    Purpose: 使用while遍历列表,循环变量使用列表下标索引来控制默认是0
    """
    index = 0
    while (index < len(list_1)):
        # comment: 
        element = list_1[index]
        print(f"列表元素是{element}")
        index +=1
    # end while
# end def

list_while(list_1)

def for_list(list_1):
    """
    Purpose: for循环遍历列表
    """
    for x in list_1:
        # comment: 
        print(f"列表内元素是{x}")
    # end for
# end def
for_list(list_1)