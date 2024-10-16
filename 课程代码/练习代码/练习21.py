my_str = '万过薪月,员序程马黑来,nphty学'
my_str = my_str[::-1]
my_str_list = my_str.split(",")
my_word = my_str_list[1]
my_word = my_word.replace('来','')
print(type(my_word))
print(my_word)