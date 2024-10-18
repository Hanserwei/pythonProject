f = open('./测试相关文件/bill.txt','r',encoding='utf-8')
bak = open('./测试相关文件/bill.txt.bak','w',encoding='utf-8')
for line in f:
    line.replace('\n','')
    if line.count('测试') !=1:
        bak.write(line)
f.close()
bak.close()