i = 1
while i < 10:
    j = 1
    while j <= i:
        print("%d*%d=%d" % (j, i, j*i),end="\t")
        if(i==j):
            print("")
        j += 1
    i += 1
# 注意观察99乘法表的结构，主要是分为九行九列，其中行数是由第二个数字控制，列数是由第一个数字控制，那么就可以一行一行绘制。
# 对于每一行有多少列就由第二个数控制，最边上的那个，两个数字相等，这时特点，可以就此来进行换行操作。