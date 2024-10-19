from pyecharts.charts import Map
from pyecharts.options import VisualMapOpts

# 准备地图对象
map = Map()
data = [
    ('北京市',99),
    ('南京市',40),
    ('四川省',88),
    ('台湾省',57),
    ('广东省',20),
    ('西安市',70)
] # 省市名字要写全

# 添加数据
map.add('测试地图',data,'china')

# 设置全局选项
map.set_global_opts(
    visualmap_opts=VisualMapOpts(
        is_show=True,
        is_piecewise=True,
        pieces=[
            {'min':1,'max':9,'lable':'1-9','color':'#CCFFFF'},
            {'min':10,'max':99,'lable':'10-99','color':'#FF6666'},
            {'min':100,'max':500,'lable':'100-500','color':'#990033'},
        ]
    ),
)

# 绘图
map.render('map.html')