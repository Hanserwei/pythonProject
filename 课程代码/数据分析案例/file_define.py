"""
和文件相关的类定义
"""
from 课程代码.数据分析案例.data_define import DataRecorder


class FileReader:
    def read_data(self)-> list[DataRecorder]:
        """读取文件，度到的每一条数据都转换成Record对象，将他们都封装到list内返回回去"""
        pass

class DateCsvReader(FileReader):
    def __init__(self,path):
        self.path = path # 定义成员变量记录基础路径

    def read_data(self)-> list[DataRecorder]:
        f = open(self.path,'r',encoding='utf-8')
        for line in f.readlines():
            line.replace('\n','')
            data_list = line.split(',')
            record = DataRecorder(data_list[0],data_list[1],int(data_list[2]),data_list[3])
