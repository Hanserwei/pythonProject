
import pymysql

from file_define import FileReader, DataCsvReader, DataJsonReader
from data_define import DataRecorder

csv_file_reader = DataCsvReader("/home/hanserwei/Downloads/pythonProject/课程代码/数据分析案例/2011年1月销售数据.txt")
json_file_reader = DataJsonReader(
    "/home/hanserwei/Downloads/pythonProject/课程代码/数据分析案例/2011年2月销售数据JSON.txt")

jan_data: list[DataRecorder] = csv_file_reader.read_data()
feb_data: list[DataRecorder] = json_file_reader.read_data()

all_data: list[DataRecorder] = jan_data + feb_data

db = pymysql.connect(
    host='localhost',
    port=3307,
    user='root',
    passwd='wwgb1314',
    db='demo',
)

cursor = db.cursor()
for data in all_data:
    sql = """
        INSERT INTO `order` (order_date, order_id, order_money, province) 
        VALUES (%s, %s, %s, %s)
    """
    values = (data.date, data.order_id, data.money, data.province)

    cursor.execute(sql, values)

# 提交事务
db.commit()

# 关闭游标和连接
cursor.close()
db.close()