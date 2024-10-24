# 指的是方法或者函数自己调用自己

# def fun():
#     if ...():
#         fun()
#     return ...

import os
def test_os():
    print(os.listdir('.')) # 列出路径下的内容
    print(os.path.isdir('.')) # 判断指定路径是不是文件夹
    print(os.path.exists('.')) # 判断指定路径是不是存在


def get_files_recursion_from_dir(path):
    file_list = []
    if os.path.exists(path):
        for i in os.listdir(path):
            new_path = path + '/'+i
            if os.path.isdir(new_path):
                file_list += get_files_recursion_from_dir(new_path) # 进入到这说明该路径是文件夹而不是文件
            else:
                file_list.append(new_path)
    else:
        print('你他妈传入空路径搞毛！')
    return file_list


if __name__ == '__main__':
    a = get_files_recursion_from_dir('.')
    for i in a:
        print(i)