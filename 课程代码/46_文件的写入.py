# 写入文件使用write方法,将内容写入
# 使用flush方法对内容进行刷新
# 调用write方法并未将内容写入文件,而是将内容写入内存中,所以需要关闭文件或者使用flush刷入内容,避免重复操作硬盘
# w模式若文件不存在则创建文件,若文件存在则清空文件再写入
f = open('./测试相关文件/文件写入.txt','w',encoding='utf-8')
# 使用write方法写入内存
f.write('Hello World!!!!')
# 调用flush方法完成写入
f.flush()
# 注意close方法内置了flush方法
f.close()