#hello world
#可视化地图基本使用
from pyecharts import Map
#准备地图对象
Map = Map()
#准备数据
data = [
    ("浙江",100)
    ("山西",50)
    ("天津",70)
    ("北京",150)
]
#添加数据
Map.add("测试地图",data,"China")
#使用render函数生成地图
Map.render()