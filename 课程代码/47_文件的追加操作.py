# 相比于写入,区别在与模式从w改为a,a模式是在原内容的后面接着写

f = open('./测试相关文件/文件追加.txt','w',encoding='utf-8')
f.write('我是帅帅维!')
f.close()

f = open('./测试相关文件/文件追加.txt','a',encoding='utf-8')
f.write('\n')
f.write('来自西南交大')
f.close()