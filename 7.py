# python基础综合案例
# 通过案例巩固基础语法，熟练语法的使用
# 折线图
# json   是一种在各种编程语言中流通的数据格式负责不同编程语言中的数据传递与交互 可类比为国际通用语言英语 本质上是特定格式的字符串
# 应用举例 可将python格式数据转为json格式数据再转化为C语言格式数据  也可反向进行
import json
data=[{"name=":"老王","age":18},{"name":"sam","age":19}]# 要进行转化的数据的格式需要满足一定要求 要以字典的形式或列表内嵌套字典
datajson=json.dumps(data,ensure_ascii=False)# 转化为json格式
print(type(datajson))
print(datajson)# 结果中的中文字符会以Unicode的编码呈现   进行转化时添加ensure_ascii=False可以将中文字符以原样保留


jsondata=json.loads(datajson)# 还原
print(type(jsondata))
print(jsondata)

# pyecharts模块   要做出数据可视化效果图，可以借用pyecharts模块  使用时要自行安装
# Echarts 由百度开源  pyecharts供python语言使用  官网pyecharts.org
# 官方画廊 https://gallery.pyecharts.org/#/README 可以查看多种图表，及其代码和执行效果
# 入门  基础折线图
from pyecharts.charts import Line# 导包，导入line功能构建折线图对象
from pyecharts.options import TitleOpts,LegendOpts,ToolboxOpts,VisualMapOpts  # 导入之后要用的全局配置选项
line=Line()# 得到折线图对象
line.add_xaxis(["china","us","uk"])# 添加x轴
line.add_yaxis("GDP",[30,20,10])# 添加名称和y轴

# 设置全局配置选项 通过set_global_opts方法来设置
line.set_global_opts(
    title_opts=TitleOpts(title="GDP展示",pos_left="center",pos_bottom="1%"),  # pos为position pos_left为设定题目距离图表左边的位置  pos_bottom为设定题目距离图表底部的位置
    legend_opts=LegendOpts(is_show=True),# 控制图列
    toolbox_opts=ToolboxOpts(is_show=True),# 显示工具箱
    visualmap_opts=VisualMapOpts(is_show=True),
)
line.render()# 会在左侧生成<>render.html  点击进入后再点击右上角的浏览器符号可以选择浏览器把生成的图表打开





# 懒人网站  ab137.com   输入文本，可以直接明了地查看复杂的嵌套关系
"""
演示可视化需求1：折线图开发
"""
import json
from pyecharts.charts import Line
from pyecharts.options import TitleOpts, LabelOpts

# 处理数据
f_us = open("E:/python课程资料/可视化案例数据/折线图数据/美国.txt", "r", encoding="UTF-8")
us_data = f_us.read()   # 美国的全部内容

f_jp = open("E:/python课程资料/可视化案例数据/折线图数据/日本.txt", "r", encoding="UTF-8")
jp_data = f_jp.read()   # 日本的全部内容

f_in = open("E:/python课程资料/可视化案例数据/折线图数据/印度.txt", "r", encoding="UTF-8")
in_data = f_in.read()   # 印度的全部内容

# 去掉不合JSON规范的开头
us_data = us_data.replace("jsonp_1629344292311_69436(", "")
jp_data = jp_data.replace("jsonp_1629350871167_29498(", "")
in_data = in_data.replace("jsonp_1629350745930_63180(", "")

# 去掉不合JSON规范的结尾
us_data = us_data[:-2]
jp_data = jp_data[:-2]
in_data = in_data[:-2]

# JSON转Python字典
us_dict = json.loads(us_data)
jp_dict = json.loads(jp_data)
in_dict = json.loads(in_data)

# 获取trend key
us_trend_data = us_dict['data'][0]['trend']
jp_trend_data = jp_dict['data'][0]['trend']
in_trend_data = in_dict['data'][0]['trend']

# 获取日期数据，用于x轴，取2020年（到314下标结束）
us_x_data = us_trend_data['updateDate'][:314]
jp_x_data = jp_trend_data['updateDate'][:314]
in_x_data = in_trend_data['updateDate'][:314]

# 获取确认数据，用于y轴，取2020年（到314下标结束）
us_y_data = us_trend_data['list'][0]['data'][:314]
jp_y_data = jp_trend_data['list'][0]['data'][:314]
in_y_data = in_trend_data['list'][0]['data'][:314]

# 生成图表
line = Line()       # 构建折线图对象
# 添加x轴数据
line.add_xaxis(us_x_data)   # x轴是公用的，所以使用一个国家的数据即可
# 添加y轴数据
line.add_yaxis("美国确诊人数", us_y_data, label_opts=LabelOpts(is_show=False))     # 添加美国的y轴数据
line.add_yaxis("日本确诊人数", jp_y_data, label_opts=LabelOpts(is_show=False))     # 添加日本的y轴数据
line.add_yaxis("印度确诊人数", in_y_data, label_opts=LabelOpts(is_show=False))     # 添加印度的y轴数据

# 设置全局选项
line.set_global_opts(
    # 标题设置
    title_opts=TitleOpts(title="2020年美日印三国确诊人数对比折线图", pos_left="center", pos_bottom="1%")
)

# 调用render方法，生成图表
line.render()
# 关闭文件对象
f_us.close()
f_jp.close()
f_in.close()




#地图可视化 基础地图使用
from pyecharts.charts import Map
from pyecharts.options import VisualMapOpts
map=Map()
data=[
    ("江西省",1),# 元组类型
    ("北京市",11),
    ("上海市",22)
]
map.add("测试地图",data,"china")
map.set_global_opts(
    visualmap_opts=VisualMapOpts(
        is_show=True,
        is_piecewise=True,# 设置为True则可以手动设置不同数量范围对应的颜色，使得地图更直观  #CCFFFF为颜色的十六进制编码
        pieces=[
            {"min":1,"max":9,"label":"1-9人","color":"#CCFFFF"},
            {"min":10,"max":19,"label":"10-19人","color":"#FF6666"},
            {"min":20,"max":29,"label":"20-29人","color":"#990033"}
               ]
                                )
)

map.render()


# 全国疫情可视化
# import json
# from pyecharts.charts import Map
# from pyecharts.options import *
# f=open('E:/python课程资料/可视化案例数据/地图数据/疫情.txt',"r",encoding="UTF-8")
# data=f.read()
# f.close()# 已经读取到数据就可以关闭文件
# data_dict=json.loads(data)
# province_data_list=data_dict["areatree"][0]["children"]
# data_list=[]
# for province_data in province_data_list:
#     province_name=province_data["name"]
#     province_confirm=province_data["total"]["confirm"]
#     data_list.append((province_name,province_confirm))# 将数据整合以元组形式存入列表
# print(data_list)
# map=Map()
# map.add("各省份确诊人数",data_list,"china")
# map.set_global_opts(
#     title_opts=TitleOpts(title="全国疫情地图"),
#     visualmap_opts=VisualMapOpts(
#         is_show=True,
#         is_piecewise=True,
#         pieces=[
#             {"min":1,"max":99,"lable":"1~99人","color":"#CCFFFF"},
#             {"min":100,"max":999,"lable":"100~999人","color":"#FFFF99"},
#             {"min":1000,"max":9999,"lable":"1000~9999人","color":"#FF9966"},
#             {"min":10000,"max":99999,"lable":"10000~99999人","color":"#FF6666"},
#             {"min":100000,"max":999999,"lable":"100000~999999人","color":"#CC3333"},
#             {"min":1000000,"max":9999999,"lable":"1000000~9999999人","color":"#990033"},
#         ]
#     )
# )
# map.render("全国疫情地图")




"""
演示河南省疫情地图开发
"""
import json
from pyecharts.charts import Map
from pyecharts.options import *

# 读取文件
f = open("D:/疫情.txt", "r", encoding="UTF-8")
data = f.read()
# 关闭文件
f.close()
# 获取河南省数据
# json数据转换为python字典
data_dict = json.loads(data)
# 取到河南省数据
cities_data = data_dict["areaTree"][0]["children"][3]["children"]

# 准备数据为元组并放入list
data_list = []
for city_data in cities_data:
    city_name = city_data["name"] + "市"
    city_confirm = city_data["total"]["confirm"]
    data_list.append((city_name, city_confirm))

# 手动添加济源市的数据
data_list.append(("济源市", 5))

# 构建地图
map = Map()
map.add("河南省疫情分布", data_list, "河南")
# 设置全局选项
map.set_global_opts(
    title_opts=TitleOpts(title="河南省疫情地图"),
    visualmap_opts=VisualMapOpts(
        is_show=True,           # 是否显示
        is_piecewise=True,      # 是否分段
        pieces=[
            {"min": 1, "max": 99, "lable": "1~99人", "color": "#CCFFFF"},
            {"min": 100, "max": 999, "lable": "100~9999人", "color": "#FFFF99"},
            {"min": 1000, "max": 4999, "lable": "1000~4999人", "color": "#FF9966"},
            {"min": 5000, "max": 9999, "lable": "5000~99999人", "color": "#FF6666"},
            {"min": 10000, "max": 99999, "lable": "10000~99999人", "color": "#CC3333"},
            {"min": 100000, "lable": "100000+", "color": "#990033"},
        ]
    )
)

# 绘图
map.render("河南省疫情地图.html")





# 基础柱状图
from pyecharts.charts import Bar
from pyecharts.options import *
bar=Bar()
bar.add_xaxis(["中国","美国","英国"])
bar.add_yaxis("GDP",[30,20,10],label_opts=LabelOpts(position="right"))
#                                  label_opts=LabelOpts(position="right")用于将x和y轴翻转之后将柱状图每个柱子对应的数值的位置调整到右边
bar.reversal_axis()# 将x和y轴反转
bar.render("基础柱状图")



# 时间线相关的动态图表
# 如果说Bar，Line对象是一张图表的话，时间线就是创建一个一维的x轴，轴上的每一个点都对应一个图表对象
from pyecharts.charts import Bar,Timeline# 引用Timeline
from pyecharts.options import *
from pyecharts.globals import ThemeType # 引用主题 用于下面在创建时间线对象时修改时间线对象的主题（改变柱状图的颜色等）
bar1=Bar()
bar1.add_xaxis(["中国","美国","英国"])
bar1.add_yaxis("GDP",[30,20,10],label_opts=LabelOpts(position="right"))
#                                  label_opts=LabelOpts(position="right")用于将x和y轴翻转之后将柱状图每个柱子对应的数值的位置调整到右边
bar1.reversal_axis()# 将x和y轴反转

bar2=Bar()
bar2.add_xaxis(["中国","美国","英国"])
bar2.add_yaxis("GDP",[50,30,20],label_opts=LabelOpts(position="right"))
bar2.reversal_axis()# 将x和y轴反转

timeline=Timeline(
    {"theme":ThemeType.LIGHT}
)# 创建时间线对象
timeline.add(bar1,"2021年GDP")
timeline.add(bar2,"2022年GDP")
timeline.add_schema(       # 设置自动播放
    play_interval=1000,# 播放间隔
    is_timeline_show=True,# 显示三角形
    is_auto_play=True,# 自动播放
    is_loop_play=True# 循环播放
)
timeline.render("基础柱状图—时间线")



# GDP动态柱状图绘制
# 掌握列表的sort方法并配合lambda匿名函数完成列表排序
# 之前学过sorted函数，但此函数无法指定排序的规则  列表的sort函数  列表.sort(key=选择排序依据的函数，reverse=True/False)reverse表示是否对结果进行反转

list=[["a",11],["b",33],["c",22]]

def choose_sort_key(element):# 通过带名称的函数排序
    return element[1]#

list.sort(key=choose_sort_key,reverse=True)# 在定义的函数的作用下，sort会以获取到的列表内的每一个元素内的下标为1的元素的大小进行排序，并输出反转的结果
print(list)

list=[["a",11],["b",33],["c",22]]
list.sort(key=lambda element:element[1],reverse=True)# 通过匿名函数排序
print(list)







from pyecharts.charts import Bar, Timeline
from pyecharts.options import *
from pyecharts.globals import ThemeType

# 读取数据
f = open("E:/python课程资料/可视化案例数据/动态柱状图数据/1960-2019全球GDP数据.csv", "r", encoding="GB2312")# 注意读取的编码格式
data_lines = f.readlines()
# 关闭文件
f.close()
# 删除第一条数据
data_lines.pop(0)
# 将数据转换为字典存储，格式为：
# { 年份: [ [国家, gdp], [国家,gdp], ......  ], 年份: [ [国家, gdp], [国家,gdp], ......  ], ...... }
# { 1960: [ [美国, 123], [中国,321], ......  ], 1961: [ [美国, 123], [中国,321], ......  ], ...... }
# 先定义一个字典对象
data_dict = {}
for line in data_lines:
    year = int(line.split(",")[0])      # 年份
    country = line.split(",")[1]        # 国家
    gdp = float(line.split(",")[2])     # gdp数据  gdp过大时会以科学计数法表示，用float将其全部转化为浮点数，就不用管表示方法的问题
    # 如何判断字典里面有没有指定的key呢？
    try:
        data_dict[year].append([country, gdp])# 当一个年份刚开始时并没有该年份的key在字典中，要先给其创建一个空的value，否则直接添加会报错，这里用try来判断是否存在该年的key
    except KeyError:
        data_dict[year] = []
        data_dict[year].append([country, gdp])

# print(data_dict[1960])  # 测试取得的字典
# 创建时间线对象，并设置主题
timeline = Timeline({"theme": ThemeType.LIGHT})
# 排序年份
sorted_year_list = sorted(data_dict.keys())# 字典是无序的，不能直接用for循环，通过.keys取得字典全部的key，再将key也就是年份排序存入一个列表中
for year in sorted_year_list:# 运用在list中以排好序的年份进行循环
    data_dict[year].sort(key=lambda element: element[1], reverse=True)# 将对应年份各国的gdp取出并排序
    # 取出本年份前8名的国家
    year_data = data_dict[year][0:8]
    x_data = []
    y_data = []
    for country_gdp in year_data:
        x_data.append(country_gdp[0])   # x轴添加国家
        y_data.append(country_gdp[1] / 100000000)   # y轴添加gdp数据

    # 构建柱状图
    bar = Bar()
    x_data.reverse()# 反转数据使得gdp最高的国家在图中显示的位置最高
    y_data.reverse()# 与x数据同步反转
    bar.add_xaxis(x_data)
    bar.add_yaxis("GDP(亿)", y_data, label_opts=LabelOpts(position="right"))
    # 反转x轴和y轴
    bar.reversal_axis()
    # 设置每一年的图表的标题
    bar.set_global_opts(
        title_opts=TitleOpts(title=f"{year}年全球前8GDP数据")
    )
    timeline.add(bar, str(year))# 括号内为图表和所属年份，相当于设置时间线上点和图的对应关系，输入了每一个点的信息


# for循环每一年的数据，基于每一年的数据，创建每一年的bar对象
# 在for中，将每一年的bar对象添加到时间线中

# 设置时间线自动播放
timeline.add_schema(
    play_interval=1000,
    is_timeline_show=True,
    is_auto_play=True,
    is_loop_play=False
)
# 绘图
timeline.render("1960-2019全球GDP前8国家.html")




