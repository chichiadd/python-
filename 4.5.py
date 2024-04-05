# #pyecharts的入门使用
# #导入pyecharts包
# from pyecharts.charts import Line
# from pyecharts.options import TitleOpts
# from pyecharts.options import LegendOpts
# from pyecharts.options import ToolboxOpts
# #创建一个折线图对象
# line = Line()
# #给折线图对象添加x轴的数据
# line.add_xaxis(["Raphtalia","naohumi","hiro"])
# #给折线图对象添加y轴的数据
# line.add_yaxis("level",[70,70,50])
# #设置全局配置项
# title_opts = TitleOpts("own_level")
# legend_opts = LegendOpts(is_show = True)
# toolbox_opts = ToolboxOpts(is_show = True)
#
# #通过render方法，将代码生成为图像
# line.render()

from pyecharts import options as opts
from pyecharts.charts import Line
# 创建一个折线图对象
line = Line()
# 给折线图对象添加x轴的数据
line.add_xaxis(["Raphtalia","Naohumi","Hiro"])
# 给折线图对象添加y轴的数据
line.add_yaxis("Level",[70,70,50])
# 设置全局配置项
line.set_global_opts(
    title_opts=opts.TitleOpts(title="own_level"),
    legend_opts=opts.LegendOpts(is_show=True),
    toolbox_opts=opts.ToolboxOpts(is_show=True)
)

# 通过render方法，将代码生成为图像
line.render()
