#pyecharts的入门使用
#导入pyecharts包
from pyecharts.charts import Line
#创建一个折线图对象
line = Line()
#给折线图对象添加x轴的数据
line.add_xaxis(["Raphtalia","naohumi","hiro"])
#给折线图对象添加y轴的数据
line.add_yaxis("level",[70,70,50])
#通过render方法，将代码生成为图像
line.render()
#设置全局配置项