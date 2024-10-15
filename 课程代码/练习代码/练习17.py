# while循环
list_a = [1,2,3,4,5,6,7,8,9,10]
def while_list(list_a):
    """
    Purpose: 使用while循环
    """
    i = 0
    list_b = []
    while i < len(list_a):
        # comment: 
        if (list_a[i]%2==0):
            # comment: 
            list_b.append(list_a[i])
        # end if
        i += 1
    # end while
    print(f"组成的新列表是{list_b}")
# end def

while_list(list_a)

# for循环
list_1 = [1,2,3,4,5,6,7,8,9,10]

def for_list(list_1):
    """
    Purpose: 使用for循环
    """
    list_c = []
    for x in range(0,len(list_1)):
        # comment: 
        if (list_1[x]%2==0):
            # comment: 
            list_c.append(list_1[x])
        # end if
    # end for
    print(f"组成的新列表是{list_c}")
# end def

for_list(list_1)