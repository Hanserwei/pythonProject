def check(arg):
    """
    Purpose: arg
    """
    print("欢迎来到国电南自！")
    if (arg>37.5):
        # comment: 
        print(f"在测量体温之中你的体温为{arg}，请马上隔离！")
    else :
        # comment: 
        print(f"你的体温为{arg},属于正常体温，请进！")
    # end if
# end def
check(28)
check(39)