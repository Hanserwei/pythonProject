# 序列类型是指的是其内容可以一个个取出的一种类型，包括字符串，列表，元组，等。
# range(num)表示一个从0开始到num的数字序列，不包含num本身。range(0)表示[0,1,2,3,4]
# range(num1,num2)表示获取一个从num1开始到num2的数字序列本身，不包含num2本身。range(5,10)表示[5,6,7,8,9]
# range(num1,num2,step)表示一个从num1开始到num2的数字序列，不包含num2本身。步长为step。range(5,10,2)表示[5,7,9]
for x in range(5):
    # comment: 
    print(x)
# end for

for x in range(5,10):
    # comment: 
    print(x)
# end for

for x in range(6,10,2):
    # comment: 
    print(x)
# end for

for x in range(10):
    # comment: 
    print(f"送第{x}朵玫瑰花")
# end for