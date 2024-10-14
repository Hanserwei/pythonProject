print("欢迎来到动物园，根据身高收费，高于130cm收费，低于等于不收费。")
hight = int(input("请输入你的身高："))
price = 10
if (hight>130):
    # comment:
    print("收费%d元"%price) 
else:
    print("你免费！")
    # comment: 
# end if
print("祝你玩得愉快！")