print("欢迎来到米奇妙妙屋，儿童免费，成年收费")
price = 10
age = int(input("请输入你的年龄："))
if (age>=18):
    print("对不起，你已经成年里，收费票价%d元"%price)
    # comment: 
else:
    print("你是小孩，所有免费！")
    # comment: 
# end if