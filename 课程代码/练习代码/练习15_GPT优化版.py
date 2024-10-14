balance = 50000

def main_menu():
    """
    Purpose: 绘制主菜单
    """
    while True:
        print("--------主菜单--------")
        print("查询余额 [输入1]")
        print("存款 [输入2]")
        print("取款 [输入3]")
        print("退出 [输入4]")
        
        choice = input("请输入你的选择:")
        
        if choice == '1':
            print(check())
        elif choice == '2':
            amount = get_amount("存款")
            print(change(amount, is_withdrawal=False))
        elif choice == '3':
            amount = get_amount("取款")
            print(change(amount, is_withdrawal=True))
        elif choice == '4':
            print("退出系统")
            break
        else:
            print("无效选择，请重新输入。")

def get_amount(transaction_type):
    while True:
        try:
            amount = int(input(f"输入{transaction_type}金额: "))
            if amount < 0:
                print("金额不能为负，请重新输入。")
            else:
                return amount
        except ValueError:
            print("请输入有效的数字。")

def change(amount, is_withdrawal):
    """
    Purpose: 取款或者存款
    """
    global balance
    if is_withdrawal:
        if amount > balance:
            return f"余额不足，无法取款{amount}元，当前余额{balance}元"
        balance -= amount
        return f"取款{amount}成功，余额{balance}元"
    else:
        balance += amount
        return f"存款{amount}成功，余额{balance}元"

def check():
    """
    Purpose: 查询余额
    """
    return f"你的余额是{balance}元"

main_menu()
