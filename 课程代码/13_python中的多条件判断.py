height = int(input("输入你的身高(cm)"))
vip_level = int(input("输入你的vip等级(1~5)"))
day = int(input("请告诉我今天几号"))
price = 20
if (height<120):
    # comment: 
    print("身高低于120cm,免费游玩")
elif (vip_level>3):
    # comment: 
    print("vip等级大于3级,免费游玩")
elif (day==1):
    # comment: 
    print("今天是一号，所有免费")
else:
    # comment: 
    print("条件都不满足，需要付费%d"% price)
# end if
# 判断是互斥的，挨个匹配，若匹配则直接输出