# # continue关键字的作用是中断本次循环，进入下一个循环
# for x in range(10):
#     # comment: 
#     if (x%2==0):
#         # comment: 
#         continue
#     # end if
#     print(x)
# # end for
# # continue只能影响当层的循环。
# for y in range(10):
#     # comment: 
#     print("原神")
#     for x in range(10):
#         # comment: 
#         continue
#         print("傻逼")
#     # end for
# # end for

# # 在循环之中遇到break就直接跳出循环
# for x in range(1,101):
#     # comment: 
#     print("语句1")
#     break
#     print("语句2")
# # end for
# print("语句3")

# 同意break也可以嵌套使用，也只对最近的循环使用。
for x in range(1,5):
    # comment: 
    print("语句1")
    for y in range(1,100):
        # comment: 
        print("语句2")
        break
        print("语句3")
    # end for
    print("语句4")
# end for