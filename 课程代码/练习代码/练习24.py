with open('../测试相关文件/练习24.txt','r',encoding='utf-8') as f:
    print(f.read().count('itheima'))

with open('../测试相关文件/练习24.txt','r',encoding='utf-8') as f:
    count = 0
    for line in f:
        line = line.replace('\n','')
        # line = line.strip()
        words = line.split(" ")
        for word in words:
            if word == 'itheima':
                count += 1
    print(count)