choice_num = None
balance = 50000
choice_num = None
money = None
def main_meum():
    """
    Purpose: 绘制主菜单
    """
    global choice_num
    print("--------主菜单--------")
    print("查询余额 ",end='')
    print("[输入1]\t")
    print("存款",end='')
    print("[输入2]\t")
    print("取款",end='')
    print("[输入3]\t")
    print("退出",end='')
    print("[输入4]\t")
    choice_num = int(input("请输入你的选择:"))
    if (choice_num==1):
        # comment: 查询余额
        print(check())
        return main_meum()
    elif (choice_num==2):
        # comment: 取款存款
        global money
        money = int(input("输入金额:"))
        print(change(money))
        return main_meum()
    elif (choice_num==3):
        # comment: 取款存款
        money = int(input("输入金额:"))
        print(change(money))
        return main_meum()
    else:
        # comment: 退出
        return exit
    # end if
    return()
# end def
def change(arg):
    """
    Purpose: 取款或者存款
    """
    global balance
    if (choice_num==3):
        # comment: 
        balance -= arg
        print("----取款----")
        return(f"取款{money}成功,余额{balance}元")
    else:
        # comment: 
        balance += arg
        print("----存款----")
        return(f"存款{money}成功,余额{balance}元")
    # end if
# end def
def check():
    """
    Purpose: 查询余额
    """
    print("----查询----")
    return(f"你的余额是{balance}")
# end def
def quit():
    """
    Purpose: 退出
    """
    main_meum()
# end def
main_meum()