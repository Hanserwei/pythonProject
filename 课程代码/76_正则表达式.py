import re
s = 'python itheima'
# match只看开头符合不符合，不符合就结束
result = re.match('python', s)
print(result)
print(result.group())
print(result.span())

# search是匹配整个，但是找到一个匹配项就结束search
ss = '1python itheima python python'
result = re.search('python', ss)
print(result)

# findall可以找出全部的匹配项
result = re.findall('python', ss)
print(result)