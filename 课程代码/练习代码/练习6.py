"""
数字随机产生,范围1-10。
有三次机会猜测，通过三层嵌套判断实现。
每次猜不中，会提示猜大了或者猜小了。
"""
import random
num = random.randint(1, 10)
guess = int(input("输入你猜的数字"))
if (guess==num):
    # comment: 
    print("猜对了")
elif (guess<num):
    # comment: 
    print("猜小了！")
    guess = int(input("第二次输入你猜的数字"))
    if (guess==num):
        # comment: 
        print("猜对了！")
    elif (guess<num):
        # comment: 
        print("猜小了")
        guess=int(input("第三次输入你猜的数字"))
        if (guess==num):
            # comment: 
            print("猜对了！")
        else:
            # comment: 
            print("三次机会都每猜中？废物一个！")
        # end if
    elif (guess>num):
        # comment: 
        print("猜大了")
        guess=int(input("第三次输入你猜的数字"))
        if (guess==num):
            # comment: 
            print("猜对了！")
        else:
            # comment: 
            print("三次机会都每猜中？废物一个！")
        # end if
    # end if
elif (guess>num):
    # comment:    
    print("猜大了！")
    guess=int(input("第二次输入你猜的数字"))
    if (guess==num):
        # comment: 
        print("猜对了！")
    elif (guess<num):
        # comment: 
        print("猜小了")
        guess=int(input("第三次输入你猜的数字"))
        if (guess==num):
            # comment: 
            print("猜对了！")
        else:
            # comment: 
            print("三次机会都每猜中？废物一个！")
        # end if
    elif (guess>num):
        # comment: 
        print("猜大了")
        guess=int(input("第三次输入你猜的数字"))
        if (guess==num):
            # comment: 
            print("猜对了！")
        else:
            # comment: 
            print("三次机会都每猜中？废物一个！")
        # end if
    # end if
# end if