# 一种轻量的数据交互方式,可以用于在不同语言之间进行交互

# json数据格式可以是
# {"name":"admin","age":18}
# 也可以是
# [{"name":"admin","age":18},{"name":"root","age":18},{"name":"张三","age":18}]

# python与json数据相互转换
import json
# 准备列表,列表中每个元素都是字典将其转换成json
data = [{"name":"admin","age":18},{"name":"root","age":15},{"name":"张三","age":30}]
# 使用json.dumps将python的列表转换成json
json_data = json.dumps(data, ensure_ascii=False) # 传入第二个参数ensure_ascii = False的参数就可以保留中文
print(json_data)

# 准备一个字典,将字典转换成json格式
data2 = {"name":"admin","age":18}
json_data2 = json.dumps(data2, ensure_ascii=False)
print(json_data2)

# 将json格式的字符串转换成列表或者字典
s = '[{"name": "admin", "age": 18}, {"name": "root", "age": 15}, {"name": "张三", "age": 30}]'
l = json.loads(s)
print(l)
print(type(l))

s2 = '{"name": "admin", "age": 18}'
l2 = json.loads(s2)
print(l2)
print(type(l2))
