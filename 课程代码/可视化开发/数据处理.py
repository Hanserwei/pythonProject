# 处理数据
import json

from pyecharts.charts import Line
from pyecharts.options import TitleOpts, LabelOpts

# 处理美国数据
f_us = open('./可视化案例数据/折线图数据/美国.txt','r',encoding='utf8')
us_data = f_us.read()

f_jp = open('./可视化案例数据/折线图数据/日本.txt','r',encoding='utf8')
jp_data = f_jp.read()

f_in = open('./可视化案例数据/折线图数据/印度.txt','r',encoding='utf8')
in_data = f_in.read()

us_data = us_data.replace('jsonp_1629344292311_69436(','')
us_data = us_data[:-2]

jp_data = jp_data.replace('jsonp_1629350871167_29498(','')
jp_data = jp_data[:-2]

in_data = in_data.replace('jsonp_1629350745930_63180(','')
in_data = in_data[:-2]
# json转python字典
us_dict = json.loads(us_data)
jp_dict = json.loads(jp_data)
in_dict = json.loads(in_data)
# print(us_dict)
# print(type(us_dict))
# 获取trend key
trend_data1 = us_dict['data'][0]['trend']
trend_data2 = jp_dict['data'][0]['trend']
trend_data3 = in_dict['data'][0]['trend']
# print(trend_data)
# 获取日期数据作为x轴
x_data1 = trend_data1['updateDate'][:314]
x_data2 = trend_data2['updateDate'][:314]
x_data3 = trend_data3['updateDate'][:314]
# 获取感染数据作为y轴
y_data1 = trend_data1['list'][0]['data'][:314]
y_data2 = trend_data2['list'][0]['data'][:314]
y_data3 = trend_data3['list'][0]['data'][:314]
# print(y_data)

# 生成图表
line = Line()
# 添加X轴
line.add_xaxis(x_data1) # x轴共用
line.add_yaxis('美国确诊人数',y_data1,label_opts=LabelOpts(is_show=False))
line.add_yaxis('日本确诊人数',y_data2,label_opts=LabelOpts(is_show=False))
line.add_yaxis('印度确诊人数',y_data3,label_opts=LabelOpts(is_show=False))

# 全局配置
line.set_global_opts(
    title_opts=TitleOpts(title='2020年美日印三国确诊人数对比则线图',pos_left='center',pos_bottom='1%'),

)

# 调用render方法生成图标
line.render('疫情.html')
f_us.close()
f_jp.close()
f_in.close()