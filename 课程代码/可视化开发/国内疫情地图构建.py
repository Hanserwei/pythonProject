import json

from pyecharts.charts import Map
from pyecharts.options import VisualMapOpts, TitleOpts

f = open('./可视化案例数据/地图数据/疫情.txt','r',encoding='utf-8')
data = f.read()
f.close()

data_dict = json.loads(data)
province_data_list = data_dict['areaTree'][0]['children']

data_list = []
for province_data in province_data_list:
    province_name = province_data['name']
    province_confirm = province_data['total']['confirm']
    data_list.append((province_name, province_confirm))

namemap = {'黑龙江省':'黑龙江','吉林省':'吉林','辽宁省':'辽宁','北京市':'北京',
           '天津市':'天津','河北省':'河北','山西省':'山西','内蒙古自治区':'内蒙古',
           '上海市':'上海','江苏省':'江苏','山东省':'山东','浙江省':'浙江','安徽省':'安徽',
           '江西省':'江西','福建省':'福建','广东省':'广东','澳门特别行政区':'澳门',
           '台湾省':'台湾','香港特别行政区':'香港','西藏自治区':'西藏','广西壮族自治区':'广西',
           '海南省':'海南','河南省':'河南','湖北省':'湖北','湖南省':'湖南','陕西省':'陕西',
           '新疆维吾尔自治区':'新疆','宁夏回族自治区':'宁夏','甘肃省':'甘肃','青海省':'青海',
           '重庆市':'重庆','四川省':'四川','贵州省':'贵州','云南省':'云南'}
map = Map()
map.add('各省份确诊人数',data_list,'china',name_map=namemap)

map.set_global_opts(
    visualmap_opts=VisualMapOpts(
        is_show=True,
        is_piecewise=True,
        pieces=[
            {'min':1,'max':99,'lable':'1-99人','color':'#CCFFFF'},
            {'min':100,'max':999,'lable':'100-999人','color':'#FFFF99'},
            {'min':1000,'max':4999,'lable':'1000-9499人','color':'#FF9966'},
            {'min':5000,'max':9999,'lable':'5000-9999人','color':'#FF6666'},
            {'min':10000,'max':99999,'lable':'10000-99999人','color':'#CC3333'},
            {'min':100000,'lable':'100000以上','color':'#990033'},
        ]
    ),
    title_opts=TitleOpts(title='全国疫情地图')
)

map.render('全国疫情地图.html')