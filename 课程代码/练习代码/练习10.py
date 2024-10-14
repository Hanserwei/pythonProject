# 求1到100不包含100的偶数
count =0
for x in range(1,100):
    # comment: 
    if(x%2==0):
        count = count+1
# end for
print(count)