# 文件的操作包含打开,关闭,读写等操作
# 打开文件,使用open()函数,参数有name,mode,encoding分别为文件名,打开文件的模式(只读,只写,追加等),编码格式
# 模式:r,w,a三个模式
f = open('./测试相关文件/python.txt', 'r', encoding='utf-8') # 打开文件
print(type(f))
# 读取文件,read(num),num表示读取文件的数据长度(单位字节),若没有传入num,则表示读取全部
# print(f"读取十个字节的结果:{f.read(10)}")
# print(f"读取全部内容的结果是:{f.read()}")
# print("----------------------------------")
# 若在程序中多次调用read,则后面的read会从前一个read结束的地方继续读取

# 读取文件.readlines(),读取全部行,封装到列表中
# lines = f.readlines()
# print(f"lines的对象类型是:{type(lines)}")
# print(f"lines的对象内容是:{lines}")
# 读取到的\n表示换行符号

# 读取文件.readline()方法,每调用一次读取一行
# line1 = f.readline()
# line2 = f.readline()
# line3 = f.readline()
# print(line1)
# print(line2)
# print(line3)

# for循环读取文件
# for line in f:
#     print(line)

# 文件的关闭
# 使用.close()方法
# f.close()

# with open 语法
with open('/测试/python.txt', 'r', encoding='utf-8') as f:
    for line in f:
        print(line)

