# 构建基础折线图
from pyecharts.charts import Line
from pyecharts.options import TitleOpts, LegendOpts, TooltipOpts, VisualMapOpts, ToolboxOpts

line = Line()
line.add_xaxis(['中国','美国','日本'])
line.add_yaxis('GDP',[30,20,10])
# line.render()

# pyecharts的全局配置选项
# 使用set_global_opts方法进行配置
line.set_global_opts(
    title_opts=TitleOpts(title='各国的GDP',pos_left="center",pos_right="center",pos_bottom="1%"),
    legend_opts=LegendOpts(is_show=True),
    toolbox_opts=ToolboxOpts(is_show=True),
    visualmap_opts=VisualMapOpts(is_show=True),
)

line.render()