# 当异常都每被捕获的时候,程序就会报错
def func1():
    print('1')
    num = 1/0
    print(num)
    return num

def func2():
    print('2')
    func1()
    return

def main():
    try:
        func2()
    except Exception as e:
        print(e)
    return

main()