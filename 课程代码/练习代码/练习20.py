my_str = 'itheima itcast boxuegu'
# 统计有多少各it
print(my_str.count("it"))
# 将字符串内的空格替换成|
new_my_str = my_str.replace(' ','|')
print(new_my_str)
# 将字符串按照"|"进行分割
my_str_list = new_my_str.split('|')
print(my_str_list)