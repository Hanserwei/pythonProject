from re import findall

s = 'itheimao1 @@python2 !!666###itcast3'
import re
result = re.findall(r'\d',s) # 字符串前面带上r的标记，转义字符无效
print(result)
result2 = re,findall(r'\W',s)
print(result2)
result3 = re.findall('[a-zA-Z0-9]',s)
print(result3)