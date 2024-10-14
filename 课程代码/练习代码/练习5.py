import random
num = random.randint(0, 10)
if (int(input("输入你第一次猜的数字："))==num):
    # comment: 
    print("猜对了！")
elif (int(input("不对,请重新猜一下"))==num):
    # comment: 
    print("猜对了！")
elif (int(input("最后依次机会，再错就没办法了！"))==num):
    # comment: 
    print("猜对了！")
else:
    # comment: 
    print("铁废物，答案是%d"%num)
# end if