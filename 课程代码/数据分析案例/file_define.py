"""
和文件相关的类定义
"""
import json

from 课程代码.数据分析案例.data_define import DataRecorder


class FileReader:
    def read_data(self)-> list[DataRecorder]:
        """读取文件，度到的每一条数据都转换成Record对象，将他们都封装到list内返回回去"""
        pass

class DataCsvReader(FileReader):
    def __init__(self,path):
        self.path = path # 定义成员变量记录基础路径

    def read_data(self)-> list[DataRecorder]:
        f = open(self.path,'r',encoding='utf-8')
        record_list = []
        for line in f.readlines():
            line = line.replace('\n','')
            data_list = line.split(',')
            record = DataRecorder(data_list[0],data_list[1],int(data_list[2]),data_list[3])
            record_list.append(record)

        f.close()
        return record_list

class DataJsonReader(FileReader):
    def __init__(self,path):
        self.path = path

    def read_data(self) -> list[DataRecorder]:
        f = open(self.path,'r',encoding='utf-8')
        record_list = []
        for line in f.readlines():
            data_dict = json.loads(line)
            record = DataRecorder(data_dict['date'],data_dict['order_id'],data_dict['money'],data_dict['province'])
            record_list.append(record)

        f.close()
        return record_list

if __name__ == '__main__':
    CsvReader = DataCsvReader('./2011年1月销售数据.txt')
    JsonReader = DataJsonReader('./2011年2月销售数据JSON.txt')
    lis1 = CsvReader.read_data()
    lis2 = JsonReader.read_data()
    for i in lis1:
        print(i)

    for i in lis2:
        print(i)