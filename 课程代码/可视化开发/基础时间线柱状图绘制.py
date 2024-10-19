from pyecharts.charts import Bar, Timeline
from pyecharts.globals import ThemeType
from pyecharts.options import LabelOpts
# 绘制每一张表
bar1 = Bar()
bar1.add_xaxis(['中国','美国','英国'])
bar1.add_yaxis('GDP',[30,20,10],label_opts=LabelOpts(position='right'))
bar1.reversal_axis()

bar2 = Bar()
bar2.add_xaxis(['中国','美国','英国'])
bar2.add_yaxis('GDP',[40,30,20],label_opts=LabelOpts(position='right'))
bar2.reversal_axis()

bar3 = Bar()
bar3.add_xaxis(['中国','美国','英国'])
bar3.add_yaxis('GDP',[50,60,40],label_opts=LabelOpts(position='right'))
bar3.reversal_axis()
# 添加时间线对象,并设置主题
timeline = Timeline(
    {'theme':ThemeType.DARK}
)
timeline.add(bar1,'点1')
timeline.add(bar2,'点2')
timeline.add(bar3,'点3')
#设置自动播放
timeline.add_schema(
    play_interval=1000,
    is_timeline_show=True,
    is_auto_play=True,
    is_loop_play=True
)

timeline.render('基础时间线柱状图.html')