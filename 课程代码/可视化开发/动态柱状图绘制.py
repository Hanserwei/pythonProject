# 列表的排序方法,sort方法
# 列表.sort(key=选择排序的依据函数,reverse=True|False)
# 参数key,要求传入一个函数,表示将列表的每一个元素都传入函数,返回排序依据
# 参数reverse,是否反转排序结果,True表示降序,False表示升序
from pyecharts.charts import Bar, Timeline
from pyecharts.globals import ThemeType
from pyecharts.options import LabelOpts, TitleOpts

# sort方法实例
# 使用带名函数
# my_list = [['a',33],['b',55],['c',11]]
# # 定义排序方法
# def choose_sort_key(element):
#     return element[1]
#
# my_list.sort(key=choose_sort_key, reverse=True)
# print(my_list)
#
# # 使用匿名函数
# my_list.sort(key=lambda element: element[1], reverse=True)
# print(my_list)

# 数据处理
f = open('./可视化案例数据/动态柱状图数据/1960-2019全球GDP数据.csv','r',encoding='GBK')
data_lines = f.readlines()
f.close()

data_lines.pop(0)
# 将数据变成字典
data_dict = dict()
for line in data_lines:
    year = int(line.split(',')[0])
    coutry = line.split(',')[1]
    gdp = float(line.split(',')[2])
    try:
        data_dict[year].append([coutry,gdp])
    except KeyError:
        data_dict[year] = []
        data_dict[year].append([coutry,gdp])

# print(data_dict)
# 排序年份
soted_years_list = sorted(data_dict.keys())
timeline = Timeline(
    {'theme':ThemeType.DARK}
)
x_data = []
y_data = []
for year in soted_years_list:
    data_dict[year].sort(key=lambda x:x[1],reverse=True)
    # 取出本年份前8名国家
    year_data = data_dict[year][0:8]
    x_data = []
    y_data = []
    for coutry_gdp in year_data:
        x_data.append(coutry_gdp[0])
        y_data.append(round(coutry_gdp[1] / 100000000,3))

    # 构建柱状图对象
    bar = Bar()
    x_data.reverse()
    y_data.reverse()
    bar.add_xaxis(x_data)
    bar.add_yaxis('GPD(亿)',y_data,label_opts=LabelOpts(position='right',is_show=True))
    bar.reversal_axis()
    bar.set_global_opts(
        title_opts=TitleOpts(title=f"{year}年全球前8国家GDP数据"),
        xaxis_opts={"axislabel": {"is_show": False}},
        yaxis_opts = {"axislabel": {"is_show": False}}
    )
    bar.set_series_opts(label_opts=LabelOpts(position='right'))
    timeline.add(bar,str(year))

timeline.add_schema(
    play_interval=1000,
    is_timeline_show=True,
    is_auto_play=True,
    is_loop_play=True
)

# 绘图
timeline.render('1960-2019全球前8GDP国家.html')