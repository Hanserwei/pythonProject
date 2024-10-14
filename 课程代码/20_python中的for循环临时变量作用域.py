# for x in range(10):
#     # comment: 
#     print(x)
# # end for
# print(x)
# 其中x是for循环中的临时变量，可以在for循环内访问到，虽然在循环外可以被访问，但是极其不规范。
# 若在循环之前对临时变量进行定义
i = 0 
for i in range(10):
    # comment: 
    print(i)
# end for
print(i)