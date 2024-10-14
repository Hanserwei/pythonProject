print("欢迎来到米奇妙妙屋！")
if (int(input("输入你的身高："))>120):
    # comment: 
    print("身高过高需要付费。")
    print("不过若你的vip等级大于3级也可以免费")
    if (int(input("输入你的vip等级"))>3):
        # comment: 
        print("你的vip等级满足条件,免费游玩!")
    else:
        # comment: 
        print("你需要买票游玩！")
    # end if
else:
    # comment: 
    print("你太矮了，可以免费游玩！")
# end if