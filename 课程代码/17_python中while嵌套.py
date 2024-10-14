i = 1
while i < 100:
    # comment: 
    print(f"今天是第{i}天。")
    j = 1
    while j < 11:
        # comment: 
        print(f"送第{j}朵玫瑰花。")
        j += 1
    # end while
    print("小美，丢你老母！")
    i += 1
# end while
print("坚持到第%d天"%i)

# 外层大循环和内层小循环的控制变量注意区别开。内层控制内层的循环，外层控制外层的循环。
# 注意条件的设置别出现了死循环。