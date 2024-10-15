# 使用列表代替元组
t1 = ['周杰伦', 11, ['football', 'music']]

# 查询年龄的下标
for x in range(len(t1)):
    if isinstance(t1[x], int):  # 使用 isinstance 更加灵活
        print(f"下标为{x}")

# 查询学生的姓名
for y in range(len(t1)):
    if isinstance(t1[y], str):
        print(f"名字为{t1[y]}")

# 删除学生爱好的 football
for z in range(len(t1)):
    if isinstance(t1[z], list):
        t1[z].remove('football')  # 删除 'football'

# 打印删除后的爱好
for z in range(len(t1)):
    if isinstance(t1[z], list):
        print(f"删除后爱好为{t1[z]}")

# 增加爱好 coding
for w in range(len(t1)):
    if isinstance(t1[w], list):
        t1[w].append('coding')  # 增加 'coding'

# 打印增加后的爱好
for w in range(len(t1)):
    if isinstance(t1[w], list):
        print(f"增加后爱好为{t1[w]}")
