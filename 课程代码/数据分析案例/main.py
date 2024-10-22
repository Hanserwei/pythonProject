from pyecharts.charts import Bar
from pyecharts.globals import ThemeType
from pyecharts.options import TitleOpts, LabelOpts, InitOpts

from file_define import FileReader,DataCsvReader,DataJsonReader
from data_define import DataRecorder

csv_file_reader = DataCsvReader('./2011年1月销售数据.txt')
json_file_reader = DataJsonReader('./2011年2月销售数据JSON.txt')

jan_data: list[DataRecorder] = csv_file_reader.read_data()
feb_data: list[DataRecorder] = json_file_reader.read_data()

all_data: list[DataRecorder] = jan_data + feb_data

# 开始计算
data_dict = {}
for record in all_data:
    if record.date in data_dict.keys():
        data_dict[record.date] += record.money
    else:
        data_dict[record.date] = record.money

# print(data_dict)

bar = Bar(init_opts=InitOpts(theme=ThemeType.LIGHT))
bar.add_xaxis(sorted(data_dict.keys()))
# print(sorted(data_dict.keys()))
bar.add_yaxis("销售额",list(data_dict.values()),label_opts=LabelOpts(is_show=False))
bar.set_global_opts(
    title_opts=TitleOpts(title='每日销售额'),

)

bar.render()
# 就不把生成的html文件上传了，多复习，第一次接受类对象这种概念好抽象呀