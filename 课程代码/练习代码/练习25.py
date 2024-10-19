from my_utils.file_util import append_to_file
from my_utils.file_util import print_file_info
from my_utils.str_util import str_reverse
from my_utils.str_util import substr

file = '../测试相关文件/练习25.txt'
print_file_info(file)
str1 = str_reverse('123456789')
str2 = substr('0123456789',0,5)
append_to_file(file,str1)
