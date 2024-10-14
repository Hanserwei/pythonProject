# 第一小节
# i = 1
# while i < 101:
#     # comment: 
#     print("原神启动！")
#     print(i)
#     i += 1
# end while
# while后跟bool类型，可以是布尔运算，只要满足条件，就会进入while内进行操作，直到条件不满足。
# 注意必须有终止条件，否则就会进入死循环。

# 第二小节
# 设置一个1-100的随机整数，通过while循环，配合input语句，判断输入的数字是否等于随机数。
# 要求：无限次机会，每次都会提示猜大了还是猜小了，猜完之后提示猜了几次。
import random
num = random.randint(1, 100)
flag = 0
i = 1 
while (flag!=1):
    # comment: 
    guess = int(input("输入你猜的数字："))
    if (guess>num):
        # comment: 
        print("猜大了！")
        i += 1
    elif (guess==num):
        # comment: 
        print("猜对了！")
        flag = 1
        print("猜了%d次"%i)
    else:
        # comment: 
        print("猜小了！")
        i += 1
    # end if
# end while