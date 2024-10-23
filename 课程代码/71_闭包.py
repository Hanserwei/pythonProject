# 闭包是指在函数嵌套的前提之下，内部函数使用了外部函数变量，并且外部函数返回类内部函数，
# 我们把这个外部函数变量的内部函数称之为闭包
def account_create(initial_account=0):
    def atm(num,deposit=True):
        nonlocal initial_account
        if deposit:
            initial_account += num
            print(f"存款：+{num},账户余额{initial_account}")
        else:
            initial_account -= num
            print(f"取款：-{num},账户余额{initial_account}")

    return atm


fn = account_create() # 拿到atm函数对象
fn(300) # 用atm函数进行存款取款
fn(200)
fn(100,False)

# 简单的闭包
def outer(logo):
    def inner(msg):
        print(f"<{logo}>{msg}<{logo}>")
    return inner

fn1 = outer("黑马程序员")
fn1("大家好！")
fn1("学习使我快乐！")

fn2 = outer("白马程序员")
fn2("大家坏！")
fn2("工作使我伤心！")

# 目的就是内部函数使用外部的变量

# 若要在闭包中修改外部函数的变量的值，那么需要在闭包中使用nonlocal的关键字

def out(num1):
    def inner(num2):
        nonlocal num1
        num1 += num2
        print(num1)
    return inner

fn = out(9)
fn(10)
fn(10)