# 就是在函数里面调用别的函数
def func_a():
    """
    Purpose: 
    """
    print("--1--")
# end def
def func_b():
    """
    Purpose: 
    """
    func_a()
    print("--2--")
    print("--3--")
# end def
func_b()