age = int(input("输入你的年龄："))
if (age>=18):
    # comment: 
    print("成年了！进入年龄限制判断！")
    if (age<30):
        # comment:
        print("年龄小于30,符合领取条件！") 
        if (int(input("输入你的入职时长"))>2):
            # comment: 
            print("入职大于两年，可以领取！")
        elif (int(input("输入你的级别："))>3):
            # comment: 
            print("级别达到要求可以领取！")
        else:
            # comment: 
            print("你年龄符合要求但是别的条件不满足,所以无法领取！")
        # end if
    else:
        # comment: 
        print("年龄超出限制，无法领取！")
else:
    # comment: 
    print("你没有成年，所有无法领取！")
# end if