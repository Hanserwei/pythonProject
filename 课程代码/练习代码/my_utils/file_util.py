def print_file_info(file_name):
    f = None
    try:
        f = open(str(file_name), 'r', encoding='utf-8')
        print(f.read())
    except FileNotFoundError:
        print('文件不存在!')
        f = open(str(file_name), 'w', encoding='utf-8')
        print('文件已经自动创建!')
    finally:
        if f:
            f.close()

def append_to_file(file_name, data):
    f = open(str(file_name), 'a', encoding='utf-8')
    f.write(data)
    f.close()

if __name__ == '__main__':
    print_file_info('../../测试相关文件/test.txt')
    append_to_file('../../测试相关文件/test.txt','123456')
